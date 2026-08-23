"""Root URL configuration for the KwaCart project.

Mounts four application routers under their respective prefixes and
defines two lightweight inline views (``home`` and ``about``) that render
static marketing pages without requiring a dedicated views module.

URL map
-------
``/``                   → landing page (home)
``/about/``             → about page
``/admin/``             → Django admin
``/accounts/``          → accounts app (login, logout, sign-up)
``/tools/``             → tools app (catalog, draft, session, guest flows)
``/archive/``           → archive app (dashboard, detail, downloads)
``/join/``              → companion-pairing entry (3-digit code)
``/join/<code>/``       → companion-pairing redirect to guest_join
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from tools.views import pairing_entry, pairing_join

from .case_study_views import case_study_detail


# home and about are simple template-only views.  Defining them inline here
# avoids creating a dedicated views.py just for two trivial render() calls.
def home(request):
    return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')


def accessibility(request):
    return render(request, 'accessibility.html')


def learn(request):
    return render(request, 'learn.html')


def pricing(request):
    return render(request, 'pricing.html')


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('pricing/', pricing, name='pricing'),
    path('accessibility/', accessibility, name='accessibility'),
    path('learn/', learn, name='learn'),
    path('case-studies/<slug:slug>/', case_study_detail, name='case_study_detail'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('tools/', include('tools.urls')),
    path('archive/', include('archive.urls')),
    # Companion pairing — short /join/<code>/ URLs for secondary-device entry.
    path('join/', pairing_entry, name='pairing_entry'),
    path('join/<str:code>/', pairing_join, name='pairing_join'),
    # static() returns [] in production (WhiteNoise serves files instead).
    # In development it adds a URL pattern so the dev server can serve uploads.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
