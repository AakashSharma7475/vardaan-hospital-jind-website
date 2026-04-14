import os

pages_dir = r"c:\Users\LRP\Documents\vardaan hospital jind\vardaan-hospital-jind-website\pages"

for filename in os.listdir(pages_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace demo-4.html with ../index.html
        new_content = content.replace('href="demo-4.html"', 'href="../index.html"')
        new_content = new_content.replace("href='demo-4.html'", "href='../index.html'")
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
