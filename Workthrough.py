import time
import string
startup = True
print("This is my Python's workthrough")
def chaptercycle():
    time.sleep(2)
    chapter = input("Press a number, one to thirteen, or type in 'quit' to quit. ")

    if chapter == "quit":
        startup = False
        print("Goodbye!")
        
    elif chapter == "1":
        result = 0
        q1 = int(input("What is 1+1? "))
        q2 = int(input("What is 2+2? "))
        q3 = int(input("What is 3+3? "))
        q4 = int(input("What is 4+4? "))
        q5 = int(input("What is 5+5? "))
        if q1 is 2:
            result = result+1
        if q2 is 4:
            result = result+1
        if q3 is 6:
            result = result+1  
        if q4 is 8:
            result = result+1
        if q5 is 10:
            result = result+1
        print ("You got", result)
        chaptercycle()
   
    elif chapter == "2":
        print("I will say if your first number is bigger than the last one")
        time.sleep(3)
        num1 = int(input("Give me the first number "))
        num2 = int(input("Give me the second one "))
        if (num1 > num2):
            bigger = True
        else:
            bigger = False
        if (bigger is True):
            print("It is")
        else:
            print("It's not")
        chaptercycle()
    
    elif chapter == "3":
        print("Now I will use a list of words to play around")
        words = ["Hello", "I", "am", "Bob"]
        names = []
        print(words)
        time.sleep(1)
        print(words[0])
        time.sleep(1)
        print(words[1])
        time.sleep(1)
        print(words[2])
        time.sleep(1)
        print(words[3])
        time.sleep(1)
        print(words[0], words[3])
        print("I used the first and last words there, it worked")
        time.sleep(2)
        print("I can mess about with APPEND AND EXTEND")
        time.sleep(2)
        words.append("!")
        print(words)
        time.sleep(2)
        print(words[0], words[1], words[2], words[3], words[4])
        time.sleep(2)
        print("(Bob)&(!) won't join up however")
        print("Now up to the interactive")
        print("You will add whatever amount of names\nyou want to a already existing list")
        amount = int(input("So how much names do you want to add? "))
        for nextend in range(amount):
            lnames = input("Add a name ")
            names.append(lnames)
        print(names)
        chaptercycle()
    
    elif chapter == "4":
        countdown = int(10)
        while (countdown > 0):
            print (countdown)
            countdown = countdown-1
            time.sleep(1)
        print("0")
        time.sleep(1)
        print("Instead of using a lot of print() commands, I used while(),\nwhich is a loop command and it worked the same, maybe better.")
        chaptercycle()
        
    elif chapter == "5":
        option = int(input("Now press 1 or 2 "))
        if option is 1:    
            print("You pressed 1")
        elif option is 2:
            print("You pressed 2")
        print("This will be useful for this workthrough, it takes too much to go to the end")
        chaptercycle()
    
    elif chapter == "6":
        print("This is a fully working simple calculator!")
        time.sleep(1)
        print("1 is adding\n2 is subtracting\n3 is multiplying\n4 is dividing")
        time.sleep(1)
        operation = int(input("Now choose one of the actions, press a number, one to four "))
        if operation is 1:
            print("Give me two numbers to add")
            n1 = float(input("-"))
            n2 = float(input("-"))
            print("The answer is", n1+n2)
        elif operation is 2:
            print("Give me two numbers to subtract")
            n1 = float(input("-"))
            n2 = float(input("-"))
            print("The answer is", n1-n2)
        elif operation is 3:
            print("Give me two numbers to mulitply")
            n1 = float(input("-"))
            n2 = float(input("-"))
            print("The answer is", n1*n2)
        elif operation is 4:
            print("Give me two numbers to divide")
            n1 = float(input("-"))
            n2 = float(input("-"))
            print("The answer is", n1/n2)
        chaptercycle()
        
    elif chapter == "7":
        invited = ["Mark", "Christian", "Adrien", "Pedro", "8NCoupon"]
        master = ["m78as."]
        print("Only certain people are invited to the party!\nYou must be using an editor to access this")
        visitor = input("What's your name")
        if visitor in invited:
            print("Welcome!")
        elif visitor in master:
            print("The codes are-\nMark\nChristian\nAdrien\n8NCoupon")
        else:
            print("Not invited!")
        chaptercycle()
        
    elif chapter == "8":
        print("Multiplication Tables!")
        time.sleep(2)
        tt = int(input("What times table do you want to learn?"))
        aa = int(input("Up to how much?"))
        pp = int(tt*aa)
        yy = int(pp+1)
        for loopcon in range (tt,yy,tt):
            print(loopcon)
        chaptercycle()

    elif chapter == "9":
        print("Counting to 100!")
        for ten in range(0,10):
            for unit in range(0,10):
                pfinal = int(ten*10)
                final = int(pfinal+unit)
                print(final)
                time.sleep(0.1)
        print("100")
        time.sleep(1)
        print("Just to understand the double loops better")
        time.sleep(2)
        print("Here is a better example, but it's not mine,\n:(")
        time.sleep(2)
		y = int(1)
        for x in range(1,11):            
            print(x,"x",y,"=",x*y)
			y += 1
        chaptercycle()
                
    elif chapter == "10": 
        for number in range(1000000):
            square = int(number*number)
            print(square, "is the square of",number)
            if square>3969:
                break
        print("I achieved one of the tasks!")
        chaptercycle()
    
    elif chapter == "11":
        print("My way")
        r1 = int(1)
        r2 = int(0)
        print("I will calculate the factorial of a number")
        factorial = int(input("Give me one "))
        for number in range(factorial):
            r2 = r2+1
            r1 = r1*r2 
        print(r1)
        chaptercycle()

    elif chapter == "12":
        print("Not my way, but better")
        product = int(1)
        print("I will calculate the factorial of a number")
        factorial = int(input("Give me one "))
        for number in range(factorial):
            product = product*(number+1) 
        print(product)
        chaptercycle()

    elif chapter == "13":
        def cycle():
            time.sleep(1)
            decision = input("Enter proceed or quit")
            if decision == "proceed":
                cycle()
            if decision == "exit":
                chaptercycle()
        desres = int(0)
        print("This is about def")
        time.sleep(2)
        print("NOTE, use ONLY quit and proceed to respond")
        time.sleep(2)
        print("Try proceed before quitting")
        cycle()

    elif chapter == "14":
        print("This may lag")
        lag = 2
        squared = input("Do you want to proceed? Type in 'yes' or 'no'. ")
        if squared == "yes":
            while lag>0:
                lag = lag*lag
                print(lag)
                time.sleep(0.1)
        elif squared == "no":
            print("OK")
            chaptercycle()
            
    
if startup is True:
    chaptercycle()

time.sleep(2)


