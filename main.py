from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
# write_key()
def load_key():
    with open("key.key","rb") as load_key:
        key=load_key.read()
    return key
def view():
    with open("passwords.txt","r") as p:
        for line in p.readlines():
            data = line.rstrip()
            print(data)
            user_name,pasw = data.split("|")
            print(f"User: {user_name} | Password: {fer.decrypt(pasw.encode().decode())}")
def add():
    user_name = input("Enter user name")
    pas= input("Enter password")
    with open("passwords.txt","a") as p:
        p.write(user_name+" | "+ fer.encrypt(pas.encode().decode()))
def main():


    while True:
        choice = int(input("Choose\n1. View \n2. Add\n3. Quit"))
        match choice:
            case 1:
                view()
            case 2:
                add()
            case _:
                print("Invalid choice")
                continue

if __name__=="__main__":
    master_pwd = input("What is the master password")
    key = load_key() + master_pwd.encode()
    fer = Fernet(key)
    main()