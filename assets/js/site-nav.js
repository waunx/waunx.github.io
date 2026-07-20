(function () {
  "use strict";

  var nav = document.getElementById("site-nav");
  if (!nav) return;

  var masthead = document.querySelector(".masthead");
  function sectionTarget(id) {
    var anchor = document.getElementById(id);
    if (!anchor) return null;

    var heading = anchor.nextElementSibling;
    if (!heading && anchor.parentElement) heading = anchor.parentElement.nextElementSibling;
    if (heading && heading.classList.contains("section-title")) return heading;
    return anchor;
  }

  function sectionId(link) {
    var href = link.getAttribute("href") || "";
    var hashIndex = href.indexOf("#");
    if (hashIndex < 0 || hashIndex === href.length - 1) return "";

    try {
      return decodeURIComponent(href.slice(hashIndex + 1));
    } catch (error) {
      return href.slice(hashIndex + 1);
    }
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest("#site-nav a");
    if (!link) return;

    var id = sectionId(link);
    var target = sectionTarget(id);
    if (!target) return;

    event.preventDefault();
    event.stopImmediatePropagation();

    var headerHeight = masthead ? masthead.getBoundingClientRect().height : 0;
    var top = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 12;
    var root = document.documentElement;
    var previousScrollBehavior = root.style.scrollBehavior;
    root.style.scrollBehavior = "auto";
    window.scrollTo(0, Math.max(0, top));
    root.style.scrollBehavior = previousScrollBehavior;

    if (window.history && window.history.replaceState) {
      window.history.replaceState(null, "", "#" + encodeURIComponent(id));
    }
  }, true);

  var links = Array.prototype.slice.call(nav.querySelectorAll("a[href*='#']")).filter(function (link) {
    return !link.parentElement.classList.contains("masthead__menu-home-item") && sectionTarget(sectionId(link));
  });

  var ticking = false;

  function updateActiveLink() {
    ticking = false;
    var headerHeight = masthead ? masthead.getBoundingClientRect().height : 0;
    var activationLine = headerHeight + 64;
    var activeId = links.length ? sectionId(links[0]) : "";
    var closestDistance = Infinity;

    links.forEach(function (link) {
      var id = sectionId(link);
      var target = sectionTarget(id);
      if (!target) return;

      var distance = Math.abs(target.getBoundingClientRect().top - activationLine);
      if (distance < closestDistance) {
        closestDistance = distance;
        activeId = id;
      }
    });

    links.forEach(function (link) {
      link.classList.toggle("is-active", sectionId(link) === activeId);
    });
  }

  function requestUpdate() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(updateActiveLink);
  }

  window.addEventListener("scroll", requestUpdate, { passive: true });
  window.addEventListener("resize", requestUpdate);
  updateActiveLink();
}());
