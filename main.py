import json

def login(name, password):
    pass
def register(name, password):
    pass

def begin():
    global option
    print("Welcome!")
    option = input("Login or Register (login, reg): ")
    if (option != "login" and option != "reg"):
        begin()

def start(option):
    global name
    if option == "login":
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("info.json", 'r') as f:
            data = json.load(f)
        if name in data.keys():
            if password == data[str(name)]:
                print("Login Successful!")
                done()
            else:
                print("Your password was incorrect. Please try again.")
        else:
            print("Your username is incorrect. Try again. You may not have an account.")

    else:
        with open("info.json", "r") as l:
            data = json.load(l)
        while True:
            name = input("Enter your username: ")
            if name in data.keys():
                print("The username is already in use. Choose a new one.")
                continue
            else:
                break
        passlist = []
        while True:
            password = input("Enter a password: ")
            for i in password:
                passlist.append(i)
            if len(passlist) > 4:
                break
            else:
                print("The password is too short. Try again.")
                passlist = []
                continue
        data[str(name)] = str(password)
        with open("info.json", "w") as b:
            json.dump(data, b)
        print("Your account has been created!")

        done()


def done():
    print("Login Successful!")
    print("Account Details:")
    print(f"Username: {name}")

begin()
start(option)