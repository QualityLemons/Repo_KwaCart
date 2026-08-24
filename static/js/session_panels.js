/**
 * Host session panel tabs — Invite / Run / Settings.
 * Uses role=tablist buttons with data-panel matching panel-* ids.
 */
(function () {
  var tabs = document.querySelectorAll(".sh-tab");
  if (!tabs.length) return;

  function activate(name) {
    tabs.forEach(function (tab) {
      var on = tab.getAttribute("data-panel") === name;
      tab.setAttribute("aria-selected", on ? "true" : "false");
      tab.tabIndex = on ? 0 : -1;
    });
    document.querySelectorAll(".sh-panel").forEach(function (panel) {
      var on = panel.id === "panel-" + name;
      panel.hidden = !on;
      panel.classList.toggle("sh-panel--active", on);
    });
  }

  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      activate(tab.getAttribute("data-panel"));
    });
    tab.addEventListener("keydown", function (e) {
      var list = Array.prototype.slice.call(tabs);
      var i = list.indexOf(tab);
      var next = -1;
      if (e.key === "ArrowRight" || e.key === "ArrowDown") next = (i + 1) % list.length;
      if (e.key === "ArrowLeft" || e.key === "ArrowUp") next = (i - 1 + list.length) % list.length;
      if (e.key === "Home") next = 0;
      if (e.key === "End") next = list.length - 1;
      if (next < 0) return;
      e.preventDefault();
      list[next].focus();
      activate(list[next].getAttribute("data-panel"));
    });
  });

  // Honour #invite | #run | #settings hash
  var hash = (location.hash || "").replace(/^#/, "");
  if (hash === "invite" || hash === "run" || hash === "settings") {
    activate(hash);
  }
})();
