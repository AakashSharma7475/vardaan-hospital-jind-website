import os

def fix_doctor_cards(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Remove the inline style margin and other card-level overrides that are now in CSS
                target = 'style="background: #fff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); padding: 30px; margin: 10px;"'
                replacement = '' # The class "doctor-1" now handles this in vardaan-hospital.css
                
                if target in content:
                    new_content = content.replace(target, replacement)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed doctor card in: {file}")

if __name__ == "__main__":
    target_dir = r"c:\Users\MITTA\Downloads\vardaan hospital website\jthemes.net\themes\html\medservices\files"
    fix_doctor_cards(target_dir)
