(function () {
    var steps = document.querySelectorAll('.cs-step');
    var dots = document.querySelectorAll('.cs-progress-dot');
    var backBtn = document.getElementById('cs-back');
    var nextBtn = document.getElementById('cs-next');
    var countEl = document.getElementById('cs-count');
    var cta = document.getElementById('cs-cta');

    if (!steps.length || !backBtn || !nextBtn) return;

    var current = 0;
    var total = steps.length;

    function showStep(index) {
        current = Math.max(0, Math.min(index, total - 1));

        steps.forEach(function (step, i) {
            var active = i === current;
            step.classList.toggle('active', active);
            if (active) step.removeAttribute('hidden');
            else step.setAttribute('hidden', '');
        });

        dots.forEach(function (dot, i) {
            var active = i === current;
            dot.classList.toggle('active', active);
            dot.setAttribute('aria-current', active ? 'step' : 'false');
        });

        backBtn.disabled = current === 0;
        if (current === total - 1) {
            nextBtn.textContent = 'Finish';
            if (cta) cta.removeAttribute('hidden');
        } else {
            nextBtn.innerHTML = 'Next \u2192';
            if (cta) cta.setAttribute('hidden', '');
        }

        if (countEl) {
            countEl.textContent = (current + 1) + ' of ' + total;
        }
    }

    backBtn.addEventListener('click', function () {
        showStep(current - 1);
    });

    nextBtn.addEventListener('click', function () {
        if (current < total - 1) showStep(current + 1);
        else if (cta) cta.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });

    dots.forEach(function (dot) {
        dot.addEventListener('click', function () {
            var idx = parseInt(dot.getAttribute('data-step'), 10);
            if (!isNaN(idx)) showStep(idx);
        });
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight' && current < total - 1) showStep(current + 1);
        if (e.key === 'ArrowLeft' && current > 0) showStep(current - 1);
    });

    showStep(0);
}());
