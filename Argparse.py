import argparse

def Main():
    user = argparse.ArgumentParser()
    homegroup = user.add_mutually_exclusive_group()
    homegroup.add_argument("-christian","--christianlogin", action="store_true", help="Christian's account")
    homegroup.add_argument("-mark","--marklogin", action="store_true", help="Mark's account")
    homegroup.add_argument("-adrien","--adrienlogin", action="store_true", help="Adrien's account")
    user.add_argument("login", help="To enter an user account of this homegroup")
    users = user.parse_args()
    if users.christianlogin:
        code = input("Type in the code")
        if code == "2308":
            print("Welcome")
        else:
            print("Incorrect code")
    elif users.marklogin:
        code = input("Type in the code")
        if code == "9622":
            print("Welcome")
        else:
            print("Incorrect code")
    elif users.adrienlogin:
        code = input("Type in the code")
        if code == "7779":
            print("Welcome")
        else:
            print("Incorrect code")
    else:
        print("Not an exisintg user in homegroup")

if __name__ == "__main__":
            Main()




