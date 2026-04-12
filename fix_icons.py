import os
import glob

directory = r'c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices\files'
files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Fix FontAwesome broken link downloaded by HTTrack
    content = content.replace('href="../../../../use.fontawesome.com/releases/v5.7.2/css/all.css"', 'href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"')
    
    # 2. Fix the missing P: replace in demo-4.html
    content = content.replace('<p>P: <a href="tel:+919999999999">+91 99999 99999</a></p>', '<p><i class="fas fa-phone" style="margin-right: 7px; color: #fff;"></i> <a href="tel:+919999999999">+91 99999 99999</a></p>')

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {os.path.basename(file)}')

print(f"Total updated: {count}")
