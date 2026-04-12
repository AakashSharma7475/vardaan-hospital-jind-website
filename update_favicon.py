import os
import re

def update_favicon(filepath, logo_rel_path):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace favicon.ico with logo path
    new_content = re.sub(r'href=".*?favicon\.ico"', f'href="{logo_rel_path}"', content)
    
    # Update type to image/png
    new_content = new_content.replace('type="image/x-icon"', 'type="image/png"')
    
    # Update apple-touch-icons
    new_content = re.sub(r'href=".*?apple-touch-icon.*?\.png"', f'href="{logo_rel_path}"', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated favicon in: {os.path.basename(filepath)}")

def process_directory(directory, logo_rel_path):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                update_favicon(os.path.join(root, file), logo_rel_path)

if __name__ == "__main__":
    # Process the main files directory
    files_dir = r"c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices\files"
    process_directory(files_dir, "images/vardaan-cross.png")
    
    # Process the top-level index.html
    top_index = r"c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices\index.html"
    update_favicon(top_index, "files/images/vardaan-cross.png")
