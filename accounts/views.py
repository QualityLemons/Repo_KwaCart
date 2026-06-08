"""Authentication and account management views for the accounts application.

Provides sign-up, login, logout, profile (read + update), and account deletion
using Django's built-in class-based views extended with project-specific
configuration (email-only sign-up form, authenticated-user redirect on the
login page, and a fixed post-logout URL).
"""
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, ProfileEmailForm


class SignUpView(CreateView):
    """Registration form view.

    On successful submission Django creates the user and redirects to the
    login page so the new user can immediately sign in.
    """

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'


class UserLoginView(LoginView):
    """Email + password login form.

    ``redirect_authenticated_user`` sends already-logged-in visitors straight
    to their post-login destination instead of showing the form again.
    """

    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    """Log the user out and send them to the login page.

    Overrides Django's default ``next_page`` so users always land on the
    login page after logging out.
    """

    next_page = reverse_lazy('accounts:login')


@login_required
def profile_view(request):
    """Read and update the authenticated user's profile.

    Two independent forms are handled by inspecting a hidden ``action`` field:
    - ``update_email``    — saves a new email address (ProfileEmailForm)
    - ``change_password`` — updates the password (Django's PasswordChangeForm)
      and re-signs the session so the user is not immediately logged out.
    """
    user = request.user
    email_form = ProfileEmailForm(instance=user)
    password_form = PasswordChangeForm(user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_email':
            email_form = ProfileEmailForm(request.POST, instance=user)
            if email_form.is_valid():
                email_form.save()
                messages.success(request, 'Email address updated.')
                return redirect('accounts:profile')

        elif action == 'change_password':
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                updated_user = password_form.save()
                update_session_auth_hash(request, updated_user)
                messages.success(request, 'Password updated.')
                return redirect('accounts:profile')

    from archive.models import ToolInstance, ToolSession
    from django.db.models import Q
    solo_count = ToolInstance.objects.filter(
        user=user, status='archived', session__isnull=True
    ).count()
    session_count = ToolSession.objects.filter(
        Q(host=user) | Q(instances__user=user)
    ).distinct().count()

    return render(request, 'accounts/profile.html', {
        'email_form': email_form,
        'password_form': password_form,
        'solo_count': solo_count,
        'session_count': session_count,
    })


@login_required
@require_POST
def account_delete(request):
    """Permanently delete the authenticated user's account.

    Requires the hidden field ``confirm`` to equal the string ``'DELETE'``
    to guard against accidental form submissions or CSRF-style misfires.
    Deleting the user cascades to all their ``ToolSession`` and
    ``ToolInstance`` records via the database-level CASCADE constraint.
    """
    user = request.user
    if request.POST.get('confirm') == 'DELETE':
        user.delete()
        messages.success(request, 'Your account has been permanently deleted.')
        return redirect('home')
    messages.error(request, 'Account deletion was not confirmed.')
    return redirect('accounts:profile')
