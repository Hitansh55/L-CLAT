import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if gsap is missing
    if 'gsap.min.js' not in content:
        # We need to insert GSAP before cursor.js
        gsap_scripts = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>\n'
        content = content.replace('<script src="cursor.js"></script>', gsap_scripts + '<script src="cursor.js"></script>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("GSAP added to HTML files.")
