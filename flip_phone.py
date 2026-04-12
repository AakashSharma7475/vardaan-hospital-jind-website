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
    
    # Replace all instances of `fas fa-phone` to `fas fa-phone fa-flip-horizontal`
    content = content.replace('"fas fa-phone"', '"fas fa-phone fa-flip-horizontal"')
    
    # Also handle if they have additional classes or styles
    # We replaced exactly `"fas fa-phone"` which covers `<i class="fas fa-phone"></i>`.
    # Wait, my previous script added: `<i class="fas fa-phone" style="margin-right: 7px; color: #fff;"></i>`
    
    # Let's ensure we don't accidentally add it twice if run again
    if 'fa-flip-horizontal' in content:
        # We might have added it before, let's be careful.
        pass
        
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {os.path.basename(file)}')

print(f"Total updated: {count}")
