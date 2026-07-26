document.addEventListener('DOMContentLoaded', () => {
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');
    const magneticTargets = document.querySelectorAll('.magnetic-target');
    
    if (cursorDot && cursorOutline && typeof gsap !== 'undefined') {
        gsap.set(cursorDot, { xPercent: -50, yPercent: -50 });
        gsap.set(cursorOutline, { xPercent: -50, yPercent: -50 });
        
        let xTo = gsap.quickTo(cursorDot, "x", {duration: 0.1, ease: "power3"});
        let yTo = gsap.quickTo(cursorDot, "y", {duration: 0.1, ease: "power3"});
        
        let xOutlineTo = gsap.quickTo(cursorOutline, "x", {duration: 0.3, ease: "power3"});
        let yOutlineTo = gsap.quickTo(cursorOutline, "y", {duration: 0.3, ease: "power3"});

        window.addEventListener('mousemove', (e) => {
            xTo(e.clientX);
            yTo(e.clientY);
            xOutlineTo(e.clientX);
            yOutlineTo(e.clientY);
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
});
