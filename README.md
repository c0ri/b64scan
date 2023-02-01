# b64scan
Searches a directory for files containing base64 encoded strings. 
This is very useful for RedTeamers and BlueTeamers.
From a RedTeam perspective, we want to be able to scan for all files containing base64 encoded strings which may contain passwords.
From a BlueTeam perspective, we know that RedTeamers obfuscate data/shells/passwords/payloads in things like base64 encoded strings. This tool can help find those.

# Author: 
Corley Efurd - skyblueguru@gmail.com
Skyblue-Soft / https://skyblue-software.com

# Help
python3 b64scan.py -h           

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
    
usage: b64scan.py [-h] -p PATH

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Directory path to search in
