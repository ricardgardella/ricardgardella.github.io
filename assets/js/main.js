/* ===== NAV MENU ===== */
const navMenu = document.getElementById('nav-menu');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');

if (navToggle) navToggle.addEventListener('click', () => navMenu.classList.add('show-menu'));
if (navClose) navClose.addEventListener('click', () => navMenu.classList.remove('show-menu'));

document.querySelectorAll('.nav__link').forEach(link => {
    link.addEventListener('click', () => navMenu.classList.remove('show-menu'));
});

/* ===== EXPERIENCE TABS ===== */
document.querySelectorAll('.exp-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.exp-tab').forEach(t => t.classList.remove('exp-tab--active'));
        tab.classList.add('exp-tab--active');

        document.querySelectorAll('[data-content]').forEach(tl => tl.classList.add('timeline--hidden'));
        document.getElementById(tab.dataset.target).classList.remove('timeline--hidden');
    });
});

/* ===== SWIPERS ===== */
new Swiper('.trusted__container', {
    loop: true,
    spaceBetween: 48,
    autoplay: { delay: 2800, disableOnInteraction: false },
    navigation: {
        nextEl: '.trusted__container .swiper-button-next',
        prevEl: '.trusted__container .swiper-button-prev',
    },
    breakpoints: {
        568: { slidesPerView: 2, spaceBetween: 64 },
        768: { slidesPerView: 3, spaceBetween: 80 },
        1024: { slidesPerView: 4, spaceBetween: 100 },
    },
});

/* ===== ACTIVE NAV ON SCROLL ===== */
window.addEventListener('scroll', () => {
    const scrollY = window.pageYOffset;
    document.querySelectorAll('section[id]').forEach(section => {
        const top = section.offsetTop - 90;
        const id = section.getAttribute('id');
        const link = document.querySelector(`.nav__link[href="#${id}"]`);
        if (!link) return;
        if (scrollY >= top && scrollY < top + section.offsetHeight) {
            link.classList.add('active-link');
        } else {
            link.classList.remove('active-link');
        }
    });
});

/* ===== SCROLL HEADER ===== */
window.addEventListener('scroll', () => {
    document.getElementById('header').classList.toggle('scroll-header', window.scrollY >= 80);
});

/* ===== SCROLL TOP ===== */
window.addEventListener('scroll', () => {
    document.getElementById('scroll-top').classList.toggle('show-scroll', window.scrollY >= 300);
});

/* ===== THEME TOGGLE ===== */
const themeBtn = document.getElementById('theme-button');
const saved = localStorage.getItem('theme') || 'dark';

document.documentElement.setAttribute('data-theme', saved);
setThemeIcon(saved);

themeBtn.addEventListener('click', () => {
    const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    setThemeIcon(next);
});

function setThemeIcon(theme) {
    themeBtn.querySelector('i').className = theme === 'dark' ? 'uil uil-sun' : 'uil uil-moon';
}
