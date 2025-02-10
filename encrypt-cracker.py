import itertools
import os
from cryptography.fernet import Fernet

def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def crack_file(encrypted_file_path, wordlist):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    for password in wordlist:
        try:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(encrypted_data)
            print(f'Success! Password found: {password}')
            return decrypted_data
        except Exception as e:
            continue

    print('Password not found in the wordlist.')

if __name__ == "__main__":
    wordlist_path = input("Enter the path to the wordlist.txt: ")
    encrypted_file_path = input("Enter the path to the encrypted file: ")

    wordlist = load_wordlist(wordlist_path)
    crack_file(encrypted_file_path, wordlist)
