// Instituto Themis Furigo — interações globais
document.addEventListener('DOMContentLoaded', function () {

  // Menu mobile
  var toggle = document.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      document.body.classList.toggle('nav-open');
    });
  }

  // Dropdowns no mobile (clique em vez de hover)
  document.querySelectorAll('.main-nav > li').forEach(function (li) {
    var btn = li.querySelector(':scope > button');
    if (!btn) return;
    btn.addEventListener('click', function () {
      if (window.innerWidth <= 1080) {
        li.classList.toggle('open');
      }
    });
  });

  // Contador animado (números de impacto)
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    var animate = function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      var duration = 1400;
      var start = null;
      function step(ts) {
        if (!start) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        var value = Math.floor(eased * target);
        el.textContent = value.toLocaleString('pt-BR') + suffix;
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = target.toLocaleString('pt-BR') + suffix;
      }
      requestAnimationFrame(step);
    };
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animate(entry.target);
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (c) { obs.observe(c); });
  }

  // Carrossel simples (home)
  var track = document.querySelector('.carousel-track');
  if (track) {
    var slides = track.children.length;
    var index = 0;
    var prev = document.querySelector('[data-carousel-prev]');
    var next = document.querySelector('[data-carousel-next]');
    var dotsWrap = document.querySelector('[data-carousel-dots]');
    var dots = [];
    if (dotsWrap) {
      for (var i = 0; i < slides; i++) {
        var d = document.createElement('button');
        d.setAttribute('aria-label', 'Slide ' + (i + 1));
        d.addEventListener('click', function (idx) { return function () { goTo(idx); }; }(i));
        dotsWrap.appendChild(d);
        dots.push(d);
      }
    }
    function render() {
      track.style.transform = 'translateX(-' + (index * 100) + '%)';
      dots.forEach(function (d, i) { d.classList.toggle('active', i === index); });
    }
    function goTo(i) { index = (i + slides) % slides; render(); }
    if (next) next.addEventListener('click', function () { goTo(index + 1); });
    if (prev) prev.addEventListener('click', function () { goTo(index - 1); });
    render();
    setInterval(function () { goTo(index + 1); }, 6000);
  }

  // Filtro de categorias do blog
  var filterButtons = document.querySelectorAll('[data-filter]');
  var blogCards = document.querySelectorAll('[data-category]');
  if (filterButtons.length && blogCards.length) {
    filterButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filterButtons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var cat = btn.getAttribute('data-filter');
        blogCards.forEach(function (card) {
          var show = cat === 'todos' || card.getAttribute('data-category') === cat;
          card.style.display = show ? '' : 'none';
        });
      });
    });
  }

  // Doação: seleção de valor
  document.querySelectorAll('.donate-option').forEach(function (opt) {
    opt.addEventListener('click', function () {
      document.querySelectorAll('.donate-option').forEach(function (o) { o.classList.remove('active'); });
      opt.classList.add('active');
      var customInput = document.querySelector('#valor-personalizado');
      if (customInput && opt.hasAttribute('data-custom')) {
        customInput.style.display = 'block';
        customInput.focus();
      } else if (customInput) {
        customInput.style.display = 'none';
      }
    });
  });

  // Copiar chave Pix
  var pixBtn = document.querySelector('[data-copy-pix]');
  if (pixBtn) {
    pixBtn.addEventListener('click', function () {
      var key = pixBtn.getAttribute('data-copy-pix');
      navigator.clipboard.writeText(key).then(function () {
        var original = pixBtn.textContent;
        pixBtn.textContent = 'Chave copiada!';
        setTimeout(function () { pixBtn.textContent = original; }, 2200);
      });
    });
  }
});
