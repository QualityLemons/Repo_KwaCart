# Threat Model

## Project Overview

Well-Served is a Django 5 web application for structured organisational dialogue and feedback. Authenticated users can sign in with an email-based account, save solo tool drafts, run collaborative live sessions, and download generated Markdown/RTF summaries. Public visitors can view marketing pages, join a waiting list, submit feature requests, and use a limited set of free try-it tools. The production deployment runs `gunicorn` against `config.wsgi:application`, which loads `config.settings.production`; the installed production apps are `accounts`, `tools`, and `archive`.

## Assets

- **User accounts and sessions** — email addresses, password hashes, session cookies, and CSRF state. Compromise allows impersonation and access to all user-owned drafts, archive entries, and session activity.
- **Collaborative session data** — host identities, participant email addresses, live responses, archived outputs, and combined session exports. These records can contain sensitive organisational feedback and should not be exposed across unrelated accounts.
- **Solo draft and archive content** — freeform text and drawing data submitted through tools, plus generated export files stored under `media/archives/`. This is the application’s primary business data.
- **Public-contact data** — waiting-list signups and feature requests, including email addresses and optional names. This is PII and is visible to staff users.
- **Application secrets and signing material** — Django `SECRET_KEY`, admin credentials, and any environment-provided secrets. Weak or missing signing secrets would undermine session and token integrity.
- **Server storage resources** — the SQLite database and files written under `media/`. Unbounded writes can degrade availability even if confidentiality is preserved.

## Trust Boundaries

- **Browser to Django application** — all form posts, JSON requests, and session navigation cross this boundary. Client input is untrusted.
- **Public to authenticated users** — landing/about/free-try/waiting-list/feature-request pages are public, while catalog, drafts, live sessions, archive views, and downloads require authentication.
- **Authenticated user to other authenticated users** — collaborative sessions intentionally allow multiple signed-in accounts to interact. Server-side authorization must prevent one account from reading or modifying another user’s data unless the sharing model explicitly permits it.
- **Authenticated user to admin/staff** — `/admin/` and staff-only waiting-list visibility are privileged surfaces that must remain restricted to staff users.
- **Application to filesystem/database** — tool input and generated exports are persisted to SQLite and `media/`. User-controlled content must not cause unauthorized file access or unbounded storage growth.
- **Development-only to production** — incomplete packages such as `apps/`, `library/`, and similar imported skeleton modules are out of scope unless they become reachable from `INSTALLED_APPS` or routed production code. `tools.views.timer_test_page` is dev-only because it is gated on `DEBUG`.

## Scan Anchors

- **Production entry points:** `config/wsgi.py`, `config/urls.py`, `accounts/urls.py`, `tools/urls.py`, `archive/urls.py`, `archive/urls_waitinglist.py`, `archive/urls_feature_request.py`.
- **Highest-risk code areas:** `tools/views.py` (draft/session state changes), `archive/views.py` and `archive/views_downloads.py` (archive visibility and file downloads), `tools/utils.py` plus `exporters/` (filesystem writes), and `config/settings/production.py` / `config/settings/base.py` (deployment security posture).
- **Public surfaces:** `/`, `/about/`, `/waiting-list/`, `/request-a-feature/`, `/accounts/signup/`, `/accounts/login/`, and `tools/<slug>/try/` for the free tools.
- **Authenticated surfaces:** `/tools/`, draft submission/autosave routes, live session routes, `/archive/dashboard/`, archive detail/delete, and download endpoints.
- **Admin surfaces:** `/admin/` plus staff-only waiting-list visibility inside the archive dashboard.
- **Usually ignore unless proven reachable in production:** `apps/`, `library/`, `accounts/middleware.py`, `archive/access_control.py`, and `tools/_test/timer/` when `DEBUG` is false.

## Threat Categories

### Spoofing

The application relies on Django’s built-in session authentication with a custom email-based user model. Production must use a strong, secret `SECRET_KEY`, must protect authenticated routes with valid sessions, and should make password-guessing and account-enumeration abuse difficult on public auth endpoints.

### Tampering

Authenticated users can create drafts, mutate live-session state, and trigger export generation. The server must enforce ownership/host checks on every state-changing route, treat all form/JSON fields as untrusted, and avoid trusting client-provided identifiers or file references.

### Information Disclosure

The core risk is exposing one user’s archive content, collaborative-session responses, participant identities, or generated files to unrelated accounts. Archive queries, session visibility rules, and download endpoints must enforce server-side scoping. Error messages and exported artifacts must not leak secrets or internal paths.

### Denial of Service

The app accepts unauthenticated form submissions and authenticated freeform text/drawing input, then persists content to SQLite and the filesystem. Public endpoints and authenticated write paths should resist spam, brute-force, and storage-exhaustion abuse through rate limits, request-size limits, and per-user quotas where appropriate.

### Elevation of Privilege

Staff/admin capabilities and cross-user collaboration are the key privilege boundaries. The application must ensure regular users cannot access admin-only data, cannot act as another user by manipulating object IDs, and cannot rely on possession of a leaked link alone to escalate into unrelated private collaboration data unless that sharing model is explicitly intended and constrained.
