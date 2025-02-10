clear
cowsay hello hacker Not Clo Ble is a termux penetration tool with some paid tools .to purchase contact me @ whatsapp.+254768974189 Gmail.morganmilstone983@gmail.com
#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

logo=$(cat << "EOF"
 _   _       _       _____ _         ____  _
| \ | |     | |     / ____| |       |  _ \| |
|  \| | ___ | |_   | |    | | ___   | |_) | | ___
| . ` |/ _ \| __|  | |    | |/ _ \  |  _ <| |/ _ \
| |\  | (_) | |_   | |____| | (_) | | |_) | |  __/
|_| \_|\___/ \__|   \_____|_|\___/  |____/|_|\___|
EOF
)

    echo -e "\n\e[1;32m$logo\e[0m\n"
    
    echo -e "\e[1;32musage:\e[0m"
    echo "1.for ftpbrute: python ftp.py <IP> <PORT> <WORDLIST_PATH>"
    echo "2.for backdoor upload Run: python3 app.py"
    echo "3.To send anonymous message run: python chat.py"
echo "4.To perfom directory search on website run: dirsearch.sh <website-url>"
echo "5.for adminbruteforce: bash adminbrute.sh <path_to_wordlist.txt> <admin_page_url> <delay_in_seconds>  OR python adminbrute.py"
echo "6.To encrypt data: scrypt enc -f <name of file> <output name> And for decryption run: scrypt dec -f <name of the dec file> <output name>"
echo "7.for automated sql injection run: sqlmap --wizard"
echo "8.for insta and fb attack run: python social.py"
echo "9.To crack encrypted file run: python encrypt-cracker.py"
echo "10.To deface a website run: python deface.py"

    

