import os
import re

def remove_httrack(directory):
    # Regex patterns for HTTrack remnants
    patterns = [
        r'<!-- Mirrored from .*? by HTTrack Website Copier/3\.x .*? -->',
        r'<!-- Mirror and index made by HTTrack .*? -->',
        r'<meta name="generator" content="HTTrack Website Copier/3\.x">',
        r'HTTrack Website Copier'
    ]

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html") or file.endswith(".js") or file.endswith(".css"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    new_content = content
                    # First remove comments/meta tags
                    new_content = re.sub(r'<!-- Mirrored from .*? by HTTrack .*? -->', '', new_content)
                    new_content = re.sub(r'<meta name="generator" content="HTTrack .*?">', '', new_content)
                    
                    # Also check for specific HTTrack titles in the root index if we process it
                    if file == "index.html" and "HTTrack" in new_content:
                        new_content = new_content.replace("Local index - HTTrack Website Copier", "VARDAAN Hospital Jind")

                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Scrubbed HTTrack from: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    # Scrub the main website files
    target_dir = r"c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices"
    remove_httrack(target_dir)
    
    # Also scrub the root index.html if it exists
    root_dir = r"c:\Users\MITTA\Downloads\vardaan hospital website"
    # Note: the root index.html is purely an HTTrack file, maybe I should just redirect it or delete it?
    # For now, I'll just scrub it.
    remove_httrack(root_dir)
