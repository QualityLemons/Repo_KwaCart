# App namespace: 'accounts'
# Named URLs exposed by this module:
#   accounts:signup   — user registration page
#   accounts:login    — login page (referenced by login_required redirects)
#   accounts:logout   — POST-only logout endpoint
#   accounts:profile  — authenticated user's profile (read + update)
#   accounts:delete   — POST-only permanent account deletion
from django.urls import path
from .views import SignUpView, UserLoginView, UserLogoutView, account_delete, profile_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('delete/', account_delete, name='delete'),
]
