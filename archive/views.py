"""Views for the archive application.

Covers the Knowledge Bank (primary authenticated area), archive detail/delete,
and download endpoints.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Max, Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, RedirectView, TemplateView

from tools.utils import get_tool_metadata

from .models import ToolInstance, ToolSession


# ── Knowledge Bank ─────────────────────────────────────────────────────────

class KnowledgeBankView(LoginRequiredMixin, TemplateView):
    """Index page — one card per tool the user has interacted with."""

    template_name = 'archive/knowledge_bank.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user

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

        session_rows = {
            row['tool_slug']: row
            for row in ToolSession.objects.filter(
                Q(host=user) | Q(instances__user=user)
            ).distinct().values('tool_slug').annotate(
                count=Count('id', distinct=True),
                last_used=Max('created_at'),
            )
        }

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

        tools_used.sort(key=lambda x: x['last_used'], reverse=True)

        ctx['tools_used'] = tools_used
        ctx['user'] = user
        return ctx


class KnowledgeBankToolView(LoginRequiredMixin, TemplateView):
    """Drill-in page for a single tool."""

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


class ArchiveDashboardView(RedirectView):
    """Redirect old /archive/dashboard/ bookmarks to the Knowledge Bank."""
    permanent = False
    url = reverse_lazy('archive:knowledge_bank')


class ArchiveDetailView(LoginRequiredMixin, DetailView):
    """Detail view for a single ``ToolInstance`` record."""

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
