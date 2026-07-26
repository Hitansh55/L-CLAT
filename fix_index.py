import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove inline CSS for cursor
content = re.sub(r'/\*\s*Custom Cursor\s*\*/.*?/\*\s*Glassmorphism Utilities\s*\*/', '/* Glassmorphism Utilities */', content, flags=re.DOTALL)
content = re.sub(r'/\*\s*Hover Reveal Cursor\s*\*/.*?/\*\s*Animated Buttons\s*\*/', '/* Animated Buttons */', content, flags=re.DOTALL)

# Remove inline JS for cursor
content = re.sub(r'//\s*Custom Cursor Logic.*?//\s*Text Reveals', '// Text Reveals', content, flags=re.DOTALL)

# Add cursor.js to index.html if it is not there
if 'cursor.js' not in content:
    content = content.replace('</body>', '    <script type="module" src="/cursor.js"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html fixed.")
