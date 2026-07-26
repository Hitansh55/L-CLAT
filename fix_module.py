import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the script tag
    content = content.replace('<script src="cursor.js"></script>', '<script type="module" src="/cursor.js"></script>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated script tags.")
