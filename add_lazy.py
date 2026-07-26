import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add loading="lazy" to all <img> tags that don't have it
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading=' not in img_tag:
            return img_tag.replace('<img ', '<img loading="lazy" ')
        return img_tag

    content = re.sub(r'<img [^>]+>', add_lazy, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Lazy loading added to images.")
