import hashlib

def crack_password(hash_to_crack, wordlist_path):
    try:
        with open(wordlist_path, 'r') as wordlist:
            for line in wordlist:
                # Remove any trailing whitespace characters
                password = line.strip()
                # Generate the SHA-1 hash of the current password
                hashed_password = hashlib.sha1(password.encode()).hexdigest()
                
                # Compare the generated hash with the hash to crack
                if hashed_password == hash_to_crack:
                    print(f"Password found: {password}")
                    return password
        print("Password not found in the wordlist.")
        return None
    except FileNotFoundError:
        print(f"Error: The file {wordlist_path} was not found.")
        return None

if __name__ == "__main__":
    # Example usage
    hash_input = input("Enter the SHA-1 hash to crack: ")
    wordlist_input = input("Enter the path to the wordlist file: ")
    crack_password(hash_input, wordlist_input)
