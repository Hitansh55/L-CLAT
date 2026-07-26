import glob

mobile_menu_html = """
<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 z-40 bg-surface/98 backdrop-blur-3xl flex flex-col items-center justify-center space-y-8 opacity-0 pointer-events-none transition-opacity duration-500">
    <a class="font-headline-lg-mobile text-headline-lg-mobile text-on-surface-variant hover:text-primary transition-colors duration-300" href="the-experience.html">Experience</a>
    <a class="font-headline-lg-mobile text-headline-lg-mobile text-on-surface-variant hover:text-primary transition-colors duration-300" href="interactive-menu.html">Menu</a>
    <a class="font-headline-lg-mobile text-headline-lg-mobile text-on-surface-variant hover:text-primary transition-colors duration-300" href="our-story.html">Story</a>
    <a class="font-headline-lg-mobile text-headline-lg-mobile text-on-surface-variant hover:text-primary transition-colors duration-300" href="contact-reservations.html">Contact</a>
    <a class="btn-ghost-gold font-label-caps text-label-caps uppercase px-8 py-4 rounded-DEFAULT mt-8 border border-primary text-primary" href="contact-reservations.html">Book a Table</a>
</div>
"""

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if mobile menu is already added
    if 'id="mobile-menu"' not in content:
        # Add id to button
        content = content.replace('<button class="md:hidden text-primary">', '<button id="mobile-menu-btn" class="md:hidden text-primary">')
        
        # Add mobile menu overlay after </nav>
        content = content.replace('</nav>', '</nav>\n' + mobile_menu_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Mobile menu added to HTML files.")
