(function () {
  "use strict";

  var DAY_MS = 24 * 60 * 60 * 1000;
  var WEEKS = 53;
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  function localDateKey(value) {
    var year = value.getFullYear();
    var month = String(value.getMonth() + 1).padStart(2, "0");
    var day = String(value.getDate()).padStart(2, "0");
    return year + "-" + month + "-" + day;
  }

  function formatNumber(value, digits) {
    return Number(value || 0).toLocaleString(undefined, {
      maximumFractionDigits: digits || 0
    });
  }

  function formatTypes(types) {
    var parts = [];
    Object.keys(types || {}).forEach(function (name) {
      parts.push(name + " × " + types[name]);
    });
    return parts.join(", ");
  }

  function tooltipFor(key, item, future) {
    if (future) return key;
    if (!item) return "No recorded activity · " + key;

    var details = [
      item.activities + (item.activities === 1 ? " activity" : " activities"),
      formatNumber(item.minutes) + " min"
    ];
    if (Number(item.distance_km) > 0) details.push(formatNumber(item.distance_km, 1) + " km");
    if (Number(item.elevation_m) > 0) details.push(formatNumber(item.elevation_m) + " m ascent");
    var types = formatTypes(item.types);
    if (types) details.push(types);
    return details.join(" · ") + " · " + key;
  }

  function renderGrid(card, payload) {
    var grid = card.querySelector("[data-heatmap-grid]");
    var scroll = card.querySelector("[data-heatmap-scroll]");
    var today = new Date();
    today.setHours(0, 0, 0, 0);
    var start = new Date(today.getTime() - ((WEEKS - 1) * 7 + today.getDay()) * DAY_MS);
    var byDate = new Map();
    (payload.days || []).forEach(function (item) {
      byDate.set(item.date, item);
    });

    grid.replaceChildren();
    var monthRow = document.createElement("div");
    monthRow.className = "training-heatmap__months";
    var lastMonth = -1;

    for (var week = 0; week < WEEKS; week += 1) {
      var weekStart = new Date(start.getTime() + week * 7 * DAY_MS);
      var month = weekStart.getMonth();
      var label = document.createElement("span");
      if (month !== lastMonth && (week === 0 || weekStart.getDate() <= 7)) {
        label.textContent = MONTHS[month];
        lastMonth = month;
      }
      monthRow.appendChild(label);
    }
    grid.appendChild(monthRow);

    var body = document.createElement("div");
    body.className = "training-heatmap__body";
    for (var column = 0; column < WEEKS; column += 1) {
      for (var row = 0; row < 7; row += 1) {
        var current = new Date(start.getTime() + (column * 7 + row) * DAY_MS);
        var key = localDateKey(current);
        var item = byDate.get(key);
        var future = current > today;
        var cell = document.createElement("span");
        cell.className = "training-heatmap__cell";
        cell.dataset.level = future ? "future" : String(item ? item.level : 0);
        cell.title = tooltipFor(key, item, future);
        cell.setAttribute("aria-label", cell.title);
        body.appendChild(cell);
      }
    }
    grid.appendChild(body);
    window.requestAnimationFrame(function () {
      scroll.scrollLeft = scroll.scrollWidth;
    });
  }

  function setStat(card, name, value) {
    var node = card.querySelector('[data-stat="' + name + '"]');
    if (node) node.textContent = value;
  }

  function render(card, payload) {
    var summary = payload.summary || {};
    setStat(card, "active-days", formatNumber(summary.active_days));
    setStat(card, "activities", formatNumber(summary.activities));
    setStat(card, "hours", formatNumber(summary.hours, 1));
    setStat(card, "distance", formatNumber(summary.distance_km, 1));
    renderGrid(card, payload);

    var status = card.querySelector("[data-heatmap-status]");
    if (!status) return;
    if (!(payload.days || []).length) {
      status.textContent = "Waiting for the first private Strava sync.";
      return;
    }
    var updated = payload.generated_at ? new Date(payload.generated_at) : null;
    status.textContent = updated && !Number.isNaN(updated.getTime())
      ? "Daily aggregates · updated " + updated.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" })
      : "Daily aggregates from Strava";
  }

  function fetchJson(url) {
    var separator = url.indexOf("?") === -1 ? "?" : "&";
    return fetch(url + separator + "v=" + Math.floor(Date.now() / 300000), { cache: "no-store" })
      .then(function (response) {
        if (!response.ok) throw new Error("HTTP " + response.status);
        return response.json();
      });
  }

  function initialize(card) {
    var source = card.dataset.source;
    var fallback = card.dataset.fallback;
    fetchJson(source)
      .catch(function () { return fetchJson(fallback); })
      .then(function (payload) { render(card, payload); })
      .catch(function () {
        render(card, { summary: {}, days: [] });
      });
  }

  document.querySelectorAll("[data-strava-heatmap]").forEach(initialize);
}());
