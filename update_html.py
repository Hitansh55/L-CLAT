import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Append =s0 to googleusercontent images
    content = re.sub(r'(https://lh3\.googleusercontent\.com/aida-public/[^"\']+)', r'\1=s0', content)
    # Prevent double =s0
    content = content.replace('=s0=s0', '=s0')
    
    # Replace sommelier image in the-experience.html
    if filepath == 'the-experience.html':
        content = re.sub(r'https://lh3\.googleusercontent\.com/aida-public/[A-Za-z0-9_-]+=s0', lambda m: 'sommelier.png' if 'AB6AXuDoG8' in m.group(0) else m.group(0), content)

    # Insert cursor.css in <head>
    if 'cursor.css' not in content:
        content = content.replace('</head>', '    <link rel="stylesheet" href="cursor.css">\n</head>')
        
    # Insert cursor divs and JS before </body>
    if 'cursor-dot' not in content or filepath != 'index.html':
        # Remove old cursor dot/outline if they exist in index.html to avoid duplicates when appending
        content = re.sub(r'<div class="cursor-dot"></div>\s*<div class="cursor-outline"></div>\s*<div id="dish-preview-cursor"></div>', '', content)
        content = content.replace('</body>', '    <div class="cursor-dot"></div>\n    <div class="cursor-outline"></div>\n    <div id="dish-preview-cursor"></div>\n    <script src="cursor.js"></script>\n</body>')
        
    # Also clean up index.html old css and js block for cursor to avoid conflict, but cursor.css overrides nicely.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files.")
