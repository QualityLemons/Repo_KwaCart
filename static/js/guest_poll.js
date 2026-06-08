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

    /* ── Hybrid pacing banner elements ── */
    var _earlyPreviewBanner = document.getElementById('ip-early-preview');
    var _vbAacBanner        = document.getElementById('vb-aac-banner');
    var _vbGroupBanner      = document.getElementById('vb-group-banner');

    /* Reacts to inclusive_pacing + timer_started_at + verbal_breakout from each
       poll response, showing the right contextual banner to the participant.
         ip-early-preview: IP active and timer not yet started — participant
                           can start composing before the countdown begins.
         vb-aac-banner:    verbal breakout active + participant is composing —
                           reassures them their digital window is still open.
         vb-group-banner:  verbal breakout active + participant not composing —
                           prompts them to join the spoken discussion. */
    function applyHybridPacing(data) {
        var ip           = !!data.inclusive_pacing;
        var timerStarted = !!data.timer_started_at;
        var vb           = !!data.verbal_breakout;
        var composingBtn = document.getElementById('aac-composing-btn');
        var isComposing  = composingBtn &&
                           composingBtn.getAttribute('aria-pressed') === 'true';
        if (_earlyPreviewBanner) {
            _earlyPreviewBanner.style.display = (ip && !timerStarted) ? '' : 'none';
        }
        if (_vbAacBanner) {
            _vbAacBanner.style.display = (vb && isComposing) ? '' : 'none';
        }
        if (_vbGroupBanner) {
            _vbGroupBanner.style.display = (vb && !isComposing) ? '' : 'none';
        }
    }

    /* ── Announce to screen readers ── */
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
            applyHybridPacing(data);

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
