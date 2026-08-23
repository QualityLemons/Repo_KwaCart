/* ── Guest session poll ── */
/* Polls the session status endpoint every 4 seconds so guest participants
   see a smooth "waiting for host" holding state when the session closes,
   then navigate automatically to the combined results.
   The status URL is read from data-status-url on #session-announcer. */
(function () {

    var ANNOUNCE_DELAY_MS    = 50;
    var POLL_INTERVAL_MS     = 4000;
    var ERROR_THRESHOLD      = 3;
    /* Grace period before auto-navigating to results.  Long enough for the
       export pipeline to finish and for participants to read the message. */
    var RESULTS_DELAY_MS     = 8000;

    /* ── Element references ── */
    var _announcer = document.getElementById('session-announcer');
    var statusUrl  = _announcer ? _announcer.dataset.statusUrl : null;

    if (!statusUrl) return;

    /* ── State ── */
    var consecutiveErrors = 0;
    var wasReconnecting   = false;
    var sessionClosed     = false;
    var pollTimer         = null;

    function announce(msg) {
        if (!_announcer) return;
        _announcer.textContent = '';
        setTimeout(function () { _announcer.textContent = msg; }, ANNOUNCE_DELAY_MS);
    }

    /* ── Waiting overlay ── */
    function showWaitingState() {
        var overlay = document.getElementById('session-waiting-overlay');
        if (overlay) {
            overlay.removeAttribute('hidden');
        }

        /* Freeze any form fields so the participant cannot submit after close */
        document.querySelectorAll(
            '#session-waiting-overlay ~ * input, ' +
            '#session-waiting-overlay ~ * textarea, ' +
            'form input, form textarea, form select, form button'
        ).forEach(function (el) { el.disabled = true; });

        /* Reveal "View results" button with current URL so it navigates to
           the closed-results render on click */
        var viewBtn = document.getElementById('swl-view-btn');
        if (viewBtn) {
            viewBtn.href = window.location.href;
            viewBtn.removeAttribute('hidden');
        }

        /* Auto-navigate after the grace period */
        setTimeout(function () { window.location.reload(); }, RESULTS_DELAY_MS);
    }

    /* ── Poll ── */
    async function poll() {
        if (sessionClosed) return;

        try {
            var resp = await fetch(statusUrl, { credentials: 'same-origin' });
            if (!resp.ok) throw new Error('HTTP ' + resp.status);
            var data = await resp.json();

            if (consecutiveErrors >= ERROR_THRESHOLD || wasReconnecting) {
                announce('Reconnected');
                wasReconnecting = false;
            }
            consecutiveErrors = 0;

            if (data.status === 'closed') {
                sessionClosed = true;
                if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }

                announce('Session has been closed. Preparing your results.');

                /* Flush the in-progress buffer so the latest text is captured */
                if (typeof window.sessionBufferFlush === 'function') {
                    await window.sessionBufferFlush();
                }

                showWaitingState();
            }
        } catch (err) {
            consecutiveErrors += 1;
            if (consecutiveErrors >= ERROR_THRESHOLD && !wasReconnecting) {
                announce('Connection lost. Attempting to reconnect.');
                wasReconnecting = true;
            }
        }
    }

    poll();
    pollTimer = setInterval(poll, POLL_INTERVAL_MS);

}());
