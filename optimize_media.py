import os
import glob
import re
from PIL import Image

public_dir = '/Users/hitanshgupta/Desktop/Stitch/l-eclat/public'

# 1. Convert PNGs to WebP
png_files = glob.glob(os.path.join(public_dir, '*.png'))
for png in png_files:
    webp_path = png.replace('.png', '.webp')
    with Image.open(png) as img:
        img.save(webp_path, 'webp', optimize=True, quality=80)
    print(f"Converted {os.path.basename(png)} to WebP")
    # optionally remove the PNG to save space, but let's keep it just in case or remove it to force usage of webp
    os.remove(png)

# 2. Update HTML files and inject CSS for hardware acceleration
html_files = glob.glob('/Users/hitanshgupta/Desktop/Stitch/l-eclat/*.html')

style_injection = """
    <style>
        .hero-img, .parallax-img, .reveal-up, .parallax-image, .reveal-text {
            will-change: transform, opacity;
            transform: translateZ(0);
        }
    </style>
</head>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace .png with .webp for our generated images
    images = ['hero_dish', 'dining_room', 'chef_portrait', 'wide_dining_room', 'scallop_carpaccio', 'beef_tartare', 'asparagus_veloute', 'sommelier']
    for img in images:
        content = content.replace(f'{img}.png', f'{img}.webp')
    
    # Inject hardware acceleration CSS before </head> if not already there
    if 'will-change: transform, opacity;' not in content:
        content = content.replace('</head>', style_injection)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Optimization complete.")
