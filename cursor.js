const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');
    const magneticTargets = document.querySelectorAll('.magnetic-target');
    
    if (cursorDot && cursorOutline && typeof gsap !== 'undefined') {
        window.addEventListener('mousemove', (e) => {
            gsap.to(cursorDot, { x: e.clientX, y: e.clientY, duration: 0.1, ease: "power2.out" });
            gsap.to(cursorOutline, { x: e.clientX, y: e.clientY, duration: 0.4, ease: "power2.out" });
        });

        magneticTargets.forEach(target => {
            target.addEventListener('mouseenter', () => {
                gsap.to(cursorOutline, { scale: 1.5, backgroundColor: 'rgba(229, 196, 131, 0.1)', duration: 0.3 });
            });
            target.addEventListener('mouseleave', () => {
                gsap.to(cursorOutline, { scale: 1, backgroundColor: 'transparent', duration: 0.3 });
                gsap.to(target, { x: 0, y: 0, duration: 0.5, ease: "elastic.out(1, 0.3)" });
            });
            target.addEventListener('mousemove', (e) => {
                const rect = target.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                gsap.to(target, { x: x * 0.2, y: y * 0.2, duration: 0.3, ease: "power2.out" });
            });
        });
    }

    // Mobile Menu Logic
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuIcon = mobileMenuBtn ? mobileMenuBtn.querySelector('span') : null;

    if (mobileMenuBtn && mobileMenu && mobileMenuIcon) {
        mobileMenuBtn.addEventListener('click', () => {
            const isOpen = mobileMenu.classList.contains('opacity-100');
            if (isOpen) {
                mobileMenu.classList.remove('opacity-100', 'pointer-events-auto');
                mobileMenu.classList.add('opacity-0', 'pointer-events-none');
                mobileMenuIcon.innerText = 'menu';
            } else {
                mobileMenu.classList.remove('opacity-0', 'pointer-events-none');
                mobileMenu.classList.add('opacity-100', 'pointer-events-auto');
                mobileMenuIcon.innerText = 'close';
            }
        });
    }