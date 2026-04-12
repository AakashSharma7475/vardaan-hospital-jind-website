import os
import glob

directory = r'c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices\files'
files = glob.glob(os.path.join(directory, '**', '*.html'), recursive=True)

count = 0
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('Dr. Rajesh Sharma', 'Dr. Ankush Berwal')
        new_content = new_content.replace('head-of-clinic.jpg', 'doctor-1.jpg')
        new_content = new_content.replace('1-800-1234-567', '+91 99999 99999')
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print('Updated:', file)
    except Exception as e:
        print(f"Failed {file}: {e}")
print(f"Total updated: {count}")
