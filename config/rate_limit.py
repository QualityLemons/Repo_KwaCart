"""Small per-IP rate-limiting helper shared by public, unauthenticated views.

Mirrors the pattern already used for pairing-code guesses in
``tools.views._pairing_rate_limited`` (kept there rather than pulled in from
here since that file is settled) so unrelated apps do not need to import from
each other. This module lives under ``config`` — not registered as a Django
app — so any app can import it without creating an import cycle.

Backed by Django's cache framework (``django.core.cache``), which defaults to
an in-process ``LocMemCache`` when no ``CACHES`` setting is configured. That
is sufficient for a single-process deployment; a multi-worker/multi-dyno
deployment would need a shared cache backend (e.g. Redis) for the limits to
apply cluster-wide.
"""
from django.core.cache import cache


def client_ip(request):
    """Best-effort client IP, honouring a single reverse-proxy hop."""
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded:
        return forwarded.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '')


def is_rate_limited(request, scope, max_attempts, window_seconds, lockout_seconds):
    """Throttle requests per client IP within a named ``scope``.

    Once a client exceeds ``max_attempts`` requests within ``window_seconds``
    it is locked out for ``lockout_seconds``, during which every call for
    that scope/IP short-circuits to ``True`` without incrementing further.
    Each call that is not already locked out counts as one attempt — callers
    should call this once per request they want throttled (e.g. once per
    POST), not per validation branch.
    """
    ip = client_ip(request) or 'unknown'
    lockout_key = f'{scope}_lockout:{ip}'
    if cache.get(lockout_key):
        return True

    attempts_key = f'{scope}_attempts:{ip}'
    attempts = cache.get(attempts_key, 0) + 1
    cache.set(attempts_key, attempts, window_seconds)
    if attempts > max_attempts:
        cache.set(lockout_key, True, lockout_seconds)
        return True
    return False
