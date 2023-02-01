import os
import base64
import argparse

def display_banner():
    banner_text = '''
.-. .-')                        .-')                ('-.         .-') _  
\  ( OO )                      ( OO ).             ( OO ).-.    ( OO ) ) 
 ;-----.\   ,--.       .---.  (_)---\_)   .-----.  / . --. /,--./ ,--,'  
 | .-.  |  /  .'      / .  |  /    _ |   '  .--./  | \-.  \ |   \ |  |\  
 | '-' /_).  / -.    / /|  |  \  :` `.   |  |('-..-'-'  |  ||    \|  | ) 
 | .-. `. | .-.  '  / / |  |_  '..`''.) /_) |OO  )\| |_.'  ||  .     |/  
 | |  \  |' \  |  |/  '-'    |.-._)   \ ||  |`-'|  |  .-.  ||  |\    |   
 | '--'  /\  `'  / `----|  |-'\       /(_'  '--'\  |  | |  ||  | \   |   
 `------'  `----'       `--'   `-----'    `-----'  `--' `--'`--'  `--'       
B64Scan.py v1.0 - Seaches a directory for files with base64 encoded strings.
Writen By: Corley Efurd (skyblueguru@gmail.com)
SkyBlue-Soft - https://skyblue-soft.com
    '''
    print(banner_text)

def search_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
                try:
                    decoded_data = base64.b64decode(data)
                except base64.binascii.Error:
                    continue
                try:
                    decoded_data = decoded_data.decode()
                    print(f"Base64 encoded string found in file: {file_path}")
                    print(f"Decoded data: {decoded_data}")
                except UnicodeDecodeError:
                    continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=display_banner())
    parser.add_argument('-p', '--path', required=True, help='Directory path to search in')
    args = parser.parse_args()
    search_directory(args.path)

