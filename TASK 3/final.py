# maintain password and user informations code 

import getpass

PASSWORD_FILE = 'passwd.txt'

def read_password_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(':') for line in file]

def write_password_file(file_path, data):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(':'.join(line) + '\n')

def encrypt_password(password):
    return ''.join(chr((ord(char) - 97 + 13) % 26 + 97) if char.islower() else char for char in password)

def decrypt_password(encrypted_password):
    return encrypt_password(encrypted_password)  # ROT-13 is its own inverse

def add_user():
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")

    users = read_password_file(PASSWORD_FILE)
    if username in [user[0] for user in users]:
        print("Cannot add. Most likely username already exists.")
        return

    encrypted_password = encrypt_password(password)
    users.append([username, real_name, encrypted_password])
    write_password_file(PASSWORD_FILE, users)
    print("User Created.")

def delete_user():
    username = input("Enter username: ")

    users = read_password_file(PASSWORD_FILE)
    users = [user for user in users if user[0] != username]

    write_password_file(PASSWORD_FILE, users)
    print("User Deleted.")

def change_password():
    username = input("User: ")
    current_password = getpass.getpass("Current Password: ")
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm: ")

    users = read_password_file(PASSWORD_FILE)
    for user in users:
        if user[0] == username:
            if decrypt_password(user[2]) != current_password:
                print("Current password is invalid.")
                return
            if new_password != confirm_password:
                print("Passwords do not match.")
                return
            user[2] = encrypt_password(new_password)
            write_password_file(PASSWORD_FILE, users)
            print("Password changed.")
            return
    print("Username not found.")

def login():
    username = input("User: ")
    password = getpass.getpass("Password: ")

    users = read_password_file(PASSWORD_FILE)
    for user in users:
        if user[0] == username and decrypt_password(user[2]) == password:
            print("Access granted.")
            return
    print("Access denied.")

if __name__ == "__main__":
    print("1. Add User")
    print("2. Delete User")
    print("3. Change Password")
    print("4. Login")

    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
        add_user()
    elif choice == '2':
        delete_user()
    elif choice == '3':
        change_password()
    elif choice == '4':
        login()
    else:
        print("Invalid choice.")
