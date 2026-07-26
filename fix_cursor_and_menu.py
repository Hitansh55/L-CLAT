import re

# Fix cursor.js
with open('cursor.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Remove DOMContentLoaded wrapper
if "document.addEventListener('DOMContentLoaded'" in js_content:
    js_content = js_content.replace("document.addEventListener('DOMContentLoaded', () => {", "")
    # Remove the last closing bracket and parenthesis
    js_content = js_content.rsplit('});', 1)[0]
    
    with open('cursor.js', 'w', encoding='utf-8') as f:
        f.write(js_content.strip())

# Fix cursor.css
with open('cursor.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if "@media (pointer: coarse)" not in css_content:
    mobile_css = """

@media (pointer: coarse) {
    html, body {
        cursor: auto !important;
    }
    .cursor-dot, .cursor-outline, #dish-preview-cursor {
        display: none !important;
    }
}
"""
    with open('cursor.css', 'w', encoding='utf-8') as f:
        f.write(css_content + mobile_css)

print("Fixed JS and CSS.")
