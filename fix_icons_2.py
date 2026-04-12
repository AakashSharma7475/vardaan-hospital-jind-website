import os
import glob
import re

directory = r'c:\Users\MITTA\Downloads\vardaan hospital website'
files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Replace any relative path before use.fontawesome.com
    content = re.sub(r'href="[^"]*?use\.fontawesome\.com/releases/v5\.7\.2/css/all\.css"', 'href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"', content)

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {os.path.basename(file)}')

print(f"Total updated: {count}")
