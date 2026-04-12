import os
import glob
import re

directory = r'c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices\files'
files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

# Regex 1: Remove social icons block
# Looks like:
# <!-- Social Icons -->
# <div class="footer-socials-links mt-20">
#   <ul class="foo-socials text-center clearfix">
#       ...
#   </ul>									
# </div>
social_pattern = re.compile(r'<!-- Social Icons -->\s*<div class="footer-socials-links mt-20">\s*<ul class="foo-socials text-center clearfix">.*?</ul>\s*</div>', re.IGNORECASE | re.DOTALL)

count = 0
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Remove social icons
        content = social_pattern.sub('', content)
        
        # 2. Replace E:
        content = content.replace('>E: <a href="mailto:info@vardaanhospital.com">', '><i class="fas fa-envelope" style="margin-right: 7px; color: #fff;"></i> <a href="mailto:info@vardaanhospital.com">')
        
        # 3. Replace P:
        content = content.replace('>P: +91 99999 99999<', '><i class="fas fa-phone" style="margin-right: 7px; color: #fff;"></i> +91 99999 99999<')

        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f'Updated {os.path.basename(file)}')
    except Exception as e:
        print(f"Failed {file}: {e}")

print(f"Total updated: {count}")
