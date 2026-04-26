// فعال کردن منوهای کشویی (dropdown)
document.querySelectorAll('.dropdown-toggle').forEach(dropdown => {
    dropdown.addEventListener('click', function(e) {
        e.preventDefault();
        let menu = this.nextElementSibling;
        if (menu && menu.classList.contains('dropdown-menu')) {
            menu.classList.toggle('show');
        }
    });
});

// بستن منو با کلیک بیرون
window.addEventListener('click', function(e) {
    if (!e.target.matches('.dropdown-toggle')) {
        document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
            menu.classList.remove('show');
        });
    }
});

// فعال کردن مدال‌ها (پنجره‌های بازشو)
document.querySelectorAll('[data-bs-toggle="modal"]').forEach(btn => {
    btn.addEventListener('click', function() {
        let modalId = this.getAttribute('data-bs-target');
        let modal = document.querySelector(modalId);
        if (modal) modal.classList.add('show');
    });
});

// بستن مدال با کلیک روی دکمه بستن
document.querySelectorAll('.btn-close').forEach(btn => {
    btn.addEventListener('click', function() {
        let modal = this.closest('.modal');
        if (modal) modal.classList.remove('show');
    });
});

// بستن مدال با کلیک روی پس‌زمینه
document.querySelectorAll('.modal').forEach(modal => {
    modal.addEventListener('click', function(e) {
        if (e.target === this) {
            this.classList.remove('show');
        }
    });
});