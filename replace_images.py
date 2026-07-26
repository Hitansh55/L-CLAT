import glob
import os
import re
import shutil

BRAIN_DIR = '/Users/hitanshgupta/.gemini/antigravity-ide/brain/312eaa5c-0035-43b8-8476-6ca634a7e730'
PUBLIC_DIR = '/Users/hitanshgupta/Desktop/Stitch/l-eclat/public'

# Map logical names to generated files
image_map = {
    'hero_dish': 'hero_dish_1785072759024.png',
    'dining_room': 'dining_room_1785072770529.png',
    'chef_portrait': 'chef_portrait_1785072850387.png',
    'wide_dining_room': 'wide_dining_room_1785072792136.png',
    'scallop_carpaccio': 'scallop_carpaccio_1785072803226.png',
    'beef_tartare': 'beef_tartare_1785072813594.png',
    'asparagus_veloute': 'asparagus_veloute_1785072823401.png'
}

url_map = {
    'AB6AXuCy7g': '/hero_dish.png',
    'AB6AXuBYVQ': '/dining_room.png',
    'AB6AXuBKV9': '/chef_portrait.png',
    'AB6AXuBsEv': '/wide_dining_room.png',
    'AB6AXuAli5': '/scallop_carpaccio.png',
    'AB6AXuD4Dp': '/beef_tartare.png',
    'AB6AXuCUvm': '/asparagus_veloute.png'
}

# Copy files
for key, filename in image_map.items():
    src = os.path.join(BRAIN_DIR, filename)
    dst = os.path.join(PUBLIC_DIR, f'{key}.png')
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {filename} to {key}.png")

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace URLs
    for url_id, new_path in url_map.items():
        # Match the full URL including `=s0` or equivalent
        pattern = r'https://lh3\.googleusercontent\.com/aida-public/' + url_id + r'[A-Za-z0-9_-]+(=s0)?'
        content = re.sub(pattern, new_path, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files updated successfully.")
