import time
import re
pins = {"Jeremy":"1057", "Suzanne":"2736", "Vicki":"4659","Jason":"5691"}
bal = {"Jeremy":"172.16", "Suzanne":"15.62", "Vicki":"23.91","Jason":"62.17"}
blocks = {"Jeremy":"0", "Suzanne":"0", "Vicki":"0", "Jason":"0"}
clients = ["Jeremy", "Suzanne", "Vicki", "Jason"]
pinrule = "^[0-9][0-9][0-9][0-9]$"
def session():
    global block
    print("Welcome to Northern Frock")
    global user
    user = input("Please enter your card.(type username) ")
    if user in clients:
        block = int(blocks[user])
        if block<3:
            pin = input("Please enter your PIN ")
            if pin == pins[user]:
                menu()
            else:
                print("Incorrect PIN")
                block = blocks[user]
                block = int(block)+1
                blocks[user] = str(block)
                if int(block)<3:
                    print(blocks[user])
                    time.sleep(2)
                    session()
                else:
                    print("Account blocked")
                    time.sleep(2)
                    session()
        else:
            print("Account is blocked")
            session()
    elif user == "99999":
        print("Bye!")
    else:
        print("Invalid card")
        time.sleep(2)
        session()

def menu():
    blocks[user] = "0"
    print("Welcome", user)
    print("1-Display balance")
    print("2-Withdraw funds")
    print("3-Deposit funds")
    print("4-Change PIN")
    print("9-Return card")
    option = input("What action do you want to execute from above? ")

    if option == "1":
        print("Your current balance is", "$"+bal[user])
        wdmx = float(bal[user])
        while wdmx>100:
            wdmx = wdmx-100
        while wdmx>80:
            wdmx = wdmx-80
        while wdmx>60:
            wdmx = wdmx-60
        while wdmx>40:
            wdmx = wdmx-40
        while wdmx>20:
            wdmx = wdmx-20
        while wdmx>10:
            wdmx = wdmx-10
        print("You can withdraw", "$"+str(float(bal[user])-wdmx))
        end()

    elif option == "2":
        print("Choose the amount you want to withdraw below")
        print("$10\n$20\n$40\n$60\n$80\n$100")
        wd = input("How much do you want to withdraw? ")
        if wd == "10":
            nwbal = float(bal[user])
            nwbal = nwbal-10
        elif wd == "20":
            nwbal = float(bal[user])
            nwbal = nwbal-20
        elif wd == "40":
            nwbal = float(bal[user])
            nwbal = nwbal-40
        elif wd == "60":
            nwbal = float(bal[user])
            nwbal = nwbal-60
        elif wd == "80":
            nwbal = float(bal[user])
            nwbal = nwbal-80
        elif wd == "100":
            nwbal = float(bal[user])
            nwbal = nwbal-100
        else:
            print("You can't withdraw this amount of money")
            time.sleep(2)
            session()
        if nwbal >= 0:
            bal[user] = str(nwbal)
            print("The money has been withdrawn")
            time.sleep(1)
            print("Your current balance is now", "$"+bal[user])
        else:
            print("You can't withdraw more")
        end()

    elif option == "3":
        dep = float(input("How much money do you want to deposit? "))
        newbal = bal[user]
        newbal = float(newbal)+dep
        bal[user] = str(newbal)
        print("The money has been deposited")
        time.sleep(2)
        print("Your current balance is now", "$"+bal[user])
        end()

    elif option == "4":
        pin = input("Please enter your PIN again ")
        if pin == pins[user]:
            newpin = input("Enter your new PIN ")
            if re.search(pinrule, newpin):
                pins[user] = newpin
                print("Your PIN has been successfully changed")
                end()
            else:
                print("Invalid format")
                time.sleep(2)
                session()
        else:
            print("Incorrect PIN")
            time.sleep(2)
            session()
    
    elif option == "9":
        print("Bye!")
        time.sleep(2)
        session()

def end():
    time.sleep(2)
    print("1-Go back to menu")
    print("9-Return card")
    decision = input("What action do you want to execute from above? ")
    if decision == "1":
        menu()
    elif decision == "9":
        print("Bye!")
        time.sleep(2)
        session()
    else:
        print("Invalid input")
        time.sleep(2)
        session()
session()

time.sleep(2)
