from cryptography.fernet import Fernet

# Run this for the first time to generate a key
# def write_key():
#     key = Fernet.generate_key()
#     with open("Mini Projects/key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def delete():
    with open('Mini Projects/passwords.txt', 'r') as f:
        lines = f.readlines()

    name = input('Account Name: ')
    with open('Mini Projects/passwords.txt', 'w') as f:
        for line in lines:
            if name not in line:
                f.write(line)

def load_key():
    file = open("Mini Projects/key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('Mini Projects/passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('Mini Projects/passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add, delete), press q to quit? ").lower()
    if mode == "q":
        print("Quiting...")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "delete":
        delete()
        print("Deleted!")
    else:
        print("Invalid mode.")
        continue