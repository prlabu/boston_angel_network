// Boston Angel Network — progressive enhancement only. The page works and reads
// fully without this file: copy/share buttons stay hidden, and every link
// still goes where it says.
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');

  function observe(elements, callback, options) {
    elements = elements.filter(Boolean);
    if (!('IntersectionObserver' in window)) {
      elements.forEach(function (el) { callback(el, true, null); });
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) { callback(entry.target, entry.isIntersecting, observer); });
    }, options);
    elements.forEach(function (el) { observer.observe(el); });
  }

  // The help steps print once, when they first come into view.
  // threshold 0 + a bottom margin works even when a tall list can never be 30% visible (zoom, landscape).
  observe([].slice.call(document.querySelectorAll('.steps')), function (el, visible, observer) {
    if (!visible) return;
    el.classList.add('seen');
    if (observer) observer.unobserve(el);
  }, { threshold: 0, rootMargin: '0px 0px -20% 0px' });

  // ---------- copy the email address; share the page ----------
  var status = document.getElementById('status');
  var announce = function (message) {
    if (!status) return;
    status.textContent = '';
    window.setTimeout(function () { status.textContent = message; }, 50);
  };

  var copyText = function (text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var field = document.createElement('textarea');
      field.value = text;
      field.setAttribute('readonly', '');
      field.style.position = 'fixed';
      field.style.opacity = '0';
      document.body.appendChild(field);
      field.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(field);
      if (ok) { resolve(); } else { reject(); }
    });
  };

  [].slice.call(document.querySelectorAll('[data-copy], [data-share]')).forEach(function (button) {
    button.addEventListener('click', function () {
      var confirm = function (message) {
        button.setAttribute('data-done', '');
        announce(message);
        window.setTimeout(function () { button.removeAttribute('data-done'); }, 2000);
      };
      if (button.hasAttribute('data-share')) {
        var url = window.location.href.split('#')[0];
        if (navigator.share) {
          navigator.share({ title: document.title, url: url }).catch(function () {});
          return;
        }
        copyText(url).then(function () { confirm('Link copied'); }, function () { announce('Copy failed. The address is ' + url); });
        return;
      }
      var text = button.getAttribute('data-copy');
      copyText(text).then(function () { confirm('Email address copied'); }, function () { announce('Copy failed. The address is ' + text); });
    });
  });

  // ---------- nav: sunflower ink under the section you are reading ----------
  var nav = document.querySelector('.nav');
  if (nav) {
    var ink = nav.querySelector('.nav-ink');
    var links = [].slice.call(nav.querySelectorAll('a'));
    var mark = function (id) {
      var link = links.filter(function (a) { return a.getAttribute('href') === '#' + id; })[0];
      links.forEach(function (a) { if (a === link) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); });
      if (!link) { ink.style.setProperty('--s', 0); return; }
      ink.style.setProperty('--x', link.offsetLeft + 'px');
      ink.style.setProperty('--s', link.offsetWidth / 100);
    };
    observe([].slice.call(document.querySelectorAll('main > section[id], .site-footer')), function (el, visible) {
      if (visible) mark(el.id);
    }, { rootMargin: '-45% 0px -50% 0px' });
    observe([document.querySelector('.hero')], function (el, visible) {
      if (visible) mark('');
    }, { rootMargin: '-45% 0px -50% 0px' });
  }

  // ---------- phones: Get help + Donate stay in reach ----------
  // The dock shows whenever the help door's own buttons are off screen (so on a
  // phone it is there from the first screen) and steps aside at the footer.
  var dock = document.querySelector('.dock');
  var helpActions = document.querySelector('.door-help .acts');
  if (dock && helpActions) {
    var helpOut = false, footerIn = false;
    var sync = function () { dock.classList.toggle('show', helpOut && !footerIn); };
    observe([helpActions], function (el, visible) { helpOut = !visible; sync(); }, { rootMargin: '0px 0px -80px 0px' });
    observe([document.querySelector('.site-footer')], function (el, visible) { footerIn = visible; sync(); });
  }
})();
