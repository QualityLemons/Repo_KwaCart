"""Views for the archive application.

Covers five areas:
- **Knowledge Bank** (``KnowledgeBankView``, ``KnowledgeBankToolView``) — the
  primary authenticated area; groups a user's activity by tool and drills into
  per-tool submissions and sessions.
- **Archive detail / delete** (``ArchiveDetailView``, ``archive_record_delete``)
  — shows a single submission and allows the owner to delete it.
- **Waiting list** (``waiting_list_signup``) — public page that collects email
  addresses; deduplicates by email using ``get_or_create``.
- **Feature requests** (``feature_request``) — public page that stores
  free-text feature ideas with an optional contact email.

Legacy redirect
---------------
``ArchiveDashboardView`` is kept as a permanent redirect to the Knowledge Bank
so that any bookmarks or stored links continue to work.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Max, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, RedirectView, TemplateView

from tools.utils import get_tool_metadata

from .forms import FeatureRequestForm, WaitingListForm
from .models import FeatureRequest, ToolInstance, ToolSession, WaitingListEntry


def _staff_only(request):
    """Return True if the request user is authenticated and is staff."""
    return request.user.is_authenticated and request.user.is_staff


# ── Knowledge Bank ─────────────────────────────────────────────────────────

class KnowledgeBankView(LoginRequiredMixin, TemplateView):
    """Index page — one card per tool the user has interacted with.

    Each card shows the tool title, total solo submissions, total sessions, and
    the date the tool was last used.  Clicking a card opens the per-tool
    drill-in view.
    """

    template_name = 'archive/knowledge_bank.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user

        # Solo submissions grouped by tool slug
        solo_rows = {
            row['tool_slug']: row
            for row in ToolInstance.objects.filter(
                user=user,
                status='archived',
                session__isnull=True,
            ).values('tool_slug').annotate(
                count=Count('id'),
                last_used=Max('submitted_at'),
            )
        }

        # Sessions the user hosted or participated in, grouped by tool slug
        session_rows = {
            row['tool_slug']: row
            for row in ToolSession.objects.filter(
                Q(host=user) | Q(instances__user=user)
            ).distinct().values('tool_slug').annotate(
                count=Count('id', distinct=True),
                last_used=Max('created_at'),
            )
        }

        # Merge into one entry per slug, enriched from the tool registry
        tools_used = []
        for slug in set(solo_rows) | set(session_rows):
            solo = solo_rows.get(slug, {})
            sess = session_rows.get(slug, {})
            meta = get_tool_metadata(slug) or {}

            solo_last = solo.get('last_used')
            sess_last = sess.get('last_used')
            if solo_last and sess_last:
                last_used = max(solo_last, sess_last)
            else:
                last_used = solo_last or sess_last

            tools_used.append({
                'slug': slug,
                'title': meta.get('title') or slug.replace('-', ' ').title(),
                'tagline': meta.get('tagline', ''),
                'icon': meta.get('icon', ''),
                'category': meta.get('category', ''),
                'solo_count': solo.get('count', 0),
                'session_count': sess.get('count', 0),
                'last_used': last_used,
            })

        # Most recently used first
        tools_used.sort(key=lambda x: x['last_used'], reverse=True)

        ctx['tools_used'] = tools_used
        ctx['user'] = user

        if user.is_staff:
            ctx['waiting_list'] = WaitingListEntry.objects.all()
            ctx['waiting_list_count'] = WaitingListEntry.objects.count()

        return ctx


class KnowledgeBankToolView(LoginRequiredMixin, TemplateView):
    """Drill-in page for a single tool.

    Shows all solo submissions and all sessions for the requesting user that
    involve the given ``tool_slug``, preserving all archive actions (view,
    preview, download, delete).
    """

    template_name = 'archive/knowledge_bank_tool.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        tool_slug = self.kwargs['tool_slug']
        meta = get_tool_metadata(tool_slug) or {}

        ctx['tool_slug'] = tool_slug
        ctx['tool_title'] = meta.get('title') or tool_slug.replace('-', ' ').title()
        ctx['tool_tagline'] = meta.get('tagline', '')

        ctx['records'] = ToolInstance.objects.filter(
            user=user,
            status='archived',
            session__isnull=True,
            tool_slug=tool_slug,
        ).order_by('-submitted_at')

        ctx['sessions'] = (
            ToolSession.objects
            .filter(Q(host=user) | Q(instances__user=user), tool_slug=tool_slug)
            .distinct()
            .order_by('-created_at')
        )

        ctx['user'] = user
        return ctx


# ── Legacy redirect ────────────────────────────────────────────────────────

class ArchiveDashboardView(RedirectView):
    """Redirect old /archive/dashboard/ bookmarks to the Knowledge Bank."""
    permanent = False
    url = reverse_lazy('archive:knowledge_bank')


# ── Archive detail / delete ────────────────────────────────────────────────

class ArchiveDetailView(LoginRequiredMixin, DetailView):
    """Detail view for a single ``ToolInstance`` record.

    The queryset is scoped to ``user=request.user`` so users cannot access
    each other's records by guessing or manipulating the primary key.
    """

    model = ToolInstance
    template_name = 'archive/detail.html'
    context_object_name = 'record'

    def get_queryset(self):
        return ToolInstance.objects.filter(user=self.request.user)


@login_required
@require_POST
def archive_record_delete(request, pk):
    instance = get_object_or_404(ToolInstance, pk=pk, user=request.user)
    tool_slug = instance.tool_slug
    instance.delete()
    messages.success(request, 'Record deleted successfully.')
    return redirect('archive:knowledge_bank_tool', tool_slug=tool_slug)


# ── Public pages ───────────────────────────────────────────────────────────

def waiting_list_signup(request):
    """Public page — collect email addresses for the waiting list."""
    result = request.GET.get('result')
    success = result in ('success', 'duplicate')
    already_on_list = result == 'duplicate'
    form = WaitingListForm()

    if request.method == 'POST':
        form = WaitingListForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower().strip()
            name = form.cleaned_data.get('name', '').strip()
            try:
                _entry, created = WaitingListEntry.objects.get_or_create(
                    email=email,
                    defaults={'name': name},
                )
                outcome = 'success' if created else 'duplicate'
                return redirect(reverse('waiting_list_signup') + '?result=' + outcome)
            except Exception:
                messages.error(
                    request,
                    'Something went wrong on our end — please try again.',
                )

    return render(request, 'archive/waiting_list_signup.html', {
        'form': form,
        'success': success,
        'already_on_list': already_on_list,
    })


def feature_request(request):
    """Public page — collect feature requests."""
    success = request.GET.get('result') == 'success'
    form = FeatureRequestForm()

    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            try:
                FeatureRequest.objects.create(
                    name=form.cleaned_data.get('name', '').strip(),
                    email=form.cleaned_data.get('email', '').strip().lower(),
                    title=form.cleaned_data['title'].strip(),
                    description=form.cleaned_data['description'].strip(),
                )
                return redirect(reverse('feature_request') + '?result=success')
            except Exception:
                messages.error(
                    request,
                    'Something went wrong on our end — please try again.',
                )

    return render(request, 'archive/feature_request.html', {
        'form': form,
        'success': success,
    })


# ── Staff management — Waiting List ────────────────────────────────────────

@login_required
def waiting_list_management(request):
    """Staff-only list of all waiting-list sign-ups with per-row delete."""
    if not _staff_only(request):
        return redirect('archive:knowledge_bank')
    entries = WaitingListEntry.objects.all().order_by('-signed_up_at')
    return render(request, 'archive/waiting_list_management.html', {
        'entries': entries,
        'count': entries.count(),
    })


@login_required
@require_POST
def waiting_list_entry_delete(request, pk):
    """Staff-only: permanently remove one waiting-list entry."""
    if not _staff_only(request):
        return redirect('archive:knowledge_bank')
    entry = get_object_or_404(WaitingListEntry, pk=pk)
    email = entry.email
    entry.delete()
    messages.success(request, f'Removed {email} from the waiting list.')
    return redirect('archive:waiting_list_management')


# ── Staff management — Feature Requests ────────────────────────────────────

@login_required
def feature_request_list(request):
    """Staff-only list of all submitted feature requests with per-row delete."""
    if not _staff_only(request):
        return redirect('archive:knowledge_bank')
    requests_qs = FeatureRequest.objects.all().order_by('-submitted_at')
    return render(request, 'archive/feature_request_list.html', {
        'requests': requests_qs,
        'count': requests_qs.count(),
    })


@login_required
@require_POST
def feature_request_delete(request, pk):
    """Staff-only: permanently delete one feature request."""
    if not _staff_only(request):
        return redirect('archive:knowledge_bank')
    fr = get_object_or_404(FeatureRequest, pk=pk)
    title = fr.title
    fr.delete()
    messages.success(request, f'Deleted feature request: "{title}".')
    return redirect('archive:feature_request_list')
