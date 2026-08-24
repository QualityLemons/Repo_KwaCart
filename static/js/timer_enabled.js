/* ── Session timer on/off ── */
/* Host toggles whether the countdown is shown for the whole room.
   Save URL is read from data-save-url on #timer-enabled-save. */
(function () {

    var toggle = document.getElementById('timer-enabled-toggle');
    var saveBtn = document.getElementById('timer-enabled-save');
    var status = document.getElementById('timer-enabled-status');

    if (!toggle || !saveBtn) return;

    var url = saveBtn.dataset.saveUrl;
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    function applyLocalVisibility(enabled) {
        var timerRegion = document.getElementById('session-timer-region');
        var banner = document.getElementById('untimed-session-banner');
        var pauseSettings = document.getElementById('pause-reminder-settings');
        if (toggle) toggle.checked = !!enabled;
        if (timerRegion) {
            if (enabled) timerRegion.removeAttribute('hidden');
            else timerRegion.setAttribute('hidden', '');
        }
        if (banner) {
            if (enabled) banner.setAttribute('hidden', '');
            else banner.removeAttribute('hidden');
        }
        if (pauseSettings) {
            if (enabled) pauseSettings.removeAttribute('hidden');
            else pauseSettings.setAttribute('hidden', '');
        }
    }

    window.applySessionTimerEnabled = applyLocalVisibility;

    saveBtn.addEventListener('click', function () {
        var enabled = toggle.checked;
        var body = new URLSearchParams();
        body.append('timer_enabled', enabled ? 'true' : 'false');
        body.append('csrfmiddlewaretoken', csrfToken);
        saveBtn.disabled = true;

        fetch(url, { method: 'POST', body: body, credentials: 'same-origin' })
            .then(function (r) { return r.json(); })
            .then(function (data) {
                saveBtn.disabled = false;
                if (data.error) {
                    status.textContent = 'Error: ' + data.error;
                    status.style.color = '#dc2626';
                    status.style.display = 'inline';
                    setTimeout(function () { status.style.display = 'none'; }, 4000);
                    return;
                }
                applyLocalVisibility(!!data.timer_enabled);
                status.textContent = data.timer_enabled
                    ? 'Timer on for everyone.'
                    : 'Timer off — room is untimed.';
                status.style.color = '#15803d';
                status.style.display = 'inline';
                setTimeout(function () { status.style.display = 'none'; }, 3000);
            })
            .catch(function () {
                saveBtn.disabled = false;
                status.textContent = 'Could not save — please try again.';
                status.style.color = '#dc2626';
                status.style.display = 'inline';
                setTimeout(function () { status.style.display = 'none'; }, 4000);
            });
    });

}());
