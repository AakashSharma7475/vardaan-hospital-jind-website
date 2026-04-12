import os
import glob
import re

directory = r'c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices\files'
files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

pattern = re.compile(r'<!-- PAGES -->.*?<!-- END MEGAMENU -->', re.IGNORECASE | re.DOTALL)

count = 0
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the matched block
        new_content, num_subs = pattern.subn('', content)
        
        if num_subs > 0:
            # Also clean up any extra blank lines left over
            new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f'Updated {file}')
    except Exception as e:
        print(f"Failed {file}: {e}")

print(f"Total updated: {count}")
