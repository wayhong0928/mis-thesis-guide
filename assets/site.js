/* 研究方法知識網絡 —— 共用互動 */
(function () {
  "use strict";

  /* 主題切換（localStorage 可能被封鎖，一律包 try/catch） */
  function readTheme() {
    try { return localStorage.getItem("rm-theme"); } catch (e) { return null; }
  }
  function writeTheme(v) {
    try { localStorage.setItem("rm-theme", v); } catch (e) { /* 忽略 */ }
  }
  var saved = readTheme();
  if (saved === "dark" || saved === "light") {
    document.documentElement.setAttribute("data-theme", saved);
  }
  var btn = document.createElement("button");
  btn.className = "themebtn";
  btn.type = "button";
  btn.setAttribute("aria-label", "切換淺色／深色");
  function paint() {
    var cur = document.documentElement.getAttribute("data-theme");
    var dark = cur === "dark" || (!cur && window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);
    btn.textContent = dark ? "☀" : "☾";
  }
  btn.addEventListener("click", function () {
    var cur = document.documentElement.getAttribute("data-theme");
    var dark = cur === "dark" || (!cur && window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);
    var next = dark ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    writeTheme(next);
    paint();
  });
  document.addEventListener("DOMContentLoaded", function () {
    document.body.appendChild(btn);
    paint();
  });

  document.addEventListener("DOMContentLoaded", function () {

    /* 手機版導覽開合 */
    var toggle = document.getElementById("navtoggle");
    var nav = document.getElementById("sidenav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        nav.classList.toggle("open");
      });
      nav.addEventListener("click", function (e) {
        if (e.target.tagName === "A") { nav.classList.remove("open"); }
      });
    }

    /* 側欄篩選 */
    var filter = document.getElementById("navfilter");
    if (filter) {
      filter.addEventListener("input", function () {
        var q = filter.value.trim().toLowerCase();
        var items = nav.querySelectorAll(".navsec li");
        items.forEach(function (li) {
          var t = (li.textContent || "").toLowerCase();
          li.classList.toggle("hide", q !== "" && t.indexOf(q) === -1);
        });
        nav.querySelectorAll(".navsec").forEach(function (sec) {
          var any = sec.querySelectorAll("li:not(.hide)").length > 0;
          sec.style.display = any ? "" : "none";
        });
      });
    }

    /* 首頁卡片篩選 */
    var home = document.getElementById("homefilter");
    if (home) {
      home.addEventListener("input", function () {
        var q = home.value.trim().toLowerCase();
        document.querySelectorAll(".card").forEach(function (c) {
          var t = (c.textContent || "").toLowerCase();
          c.classList.toggle("hide", q !== "" && t.indexOf(q) === -1);
        });
        document.querySelectorAll(".mapsec").forEach(function (sec) {
          var any = sec.querySelectorAll(".card:not(.hide)").length > 0;
          sec.style.display = any ? "" : "none";
        });
      });
    }

    /* 右側目錄的目前位置標示 */
    var toc = document.getElementById("toc");
    if (toc && "IntersectionObserver" in window) {
      var links = {};
      toc.querySelectorAll("a[href^='#']").forEach(function (a) {
        links[decodeURIComponent(a.getAttribute("href").slice(1))] = a;
      });
      var heads = document.querySelectorAll(".doc h2[id], .doc h3[id]");
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          var a = links[en.target.id];
          if (!a) { return; }
          if (en.isIntersecting) {
            Object.keys(links).forEach(function (k) { links[k].classList.remove("here"); });
            a.classList.add("here");
          }
        });
      }, { rootMargin: "0px 0px -72% 0px", threshold: 0 });
      heads.forEach(function (h) { io.observe(h); });
    }

    /* 檢查清單狀態記在本機（僅此瀏覽器，清除網站資料就沒了） */
    var key = "rm-chk:" + location.pathname.split("/").pop();
    var boxes = document.querySelectorAll("li.chk input[type=checkbox]");
    if (boxes.length) {
      var state = [];
      try { state = JSON.parse(localStorage.getItem(key) || "[]"); } catch (e) { state = []; }
      boxes.forEach(function (b, i) {
        if (state[i]) { b.checked = true; }
        b.addEventListener("change", function () {
          var s = [];
          boxes.forEach(function (x) { s.push(x.checked ? 1 : 0); });
          try { localStorage.setItem(key, JSON.stringify(s)); } catch (e) { /* 忽略 */ }
        });
      });
    }
  });
})();
