from sys import exit
import time

def learn_python():
    print("Yay! You've chosen to learn Python!")
    time.sleep(2)
    print("Today you're going to learn how to 'print' something to the screen.")
    time.sleep(2)
    print("Let's get started!")

    time.sleep(2)

    print("The command that allows you to do this in Python is the 'print()'' command!")
    time.sleep(3)
    print("'print' is a keyword in Python.")
    time.sleep(2)
    print("In fact, that's exactly how you're seeing this text!")

    time.sleep(3)

    print("Let's see if you can use it correctly.")
    print('Try typing the following characters, exactly as you see them: print("Does this really work?")')
    command = input(">>> ")
    if command == 'print("Does this really work?")':
        print("Does this really work?")
        time.sleep(2)
        print("Yay! You did it!")
        time.sleep(3)
        print("You may now tell your friends and family that you are a Python developer.")
        time.sleep(2.5)
        exit(0)
    else:
        print("Oops!! It looks like something went wrong!")
        print("Let's try again!")
        learn_python()


def learn_java():
    print("Yay! You've chosen to learn Java!")
    time.sleep(2)
    print("Today you're going to learn how to 'print' something to the screen.")
    time.sleep(2)
    print("Let's get started!")

    time.sleep(2)

    print("The command that allows you to do this in Java is the 'System.out.printIn()' command!")
    time.sleep(3)
    print("'System.out.printIn' is statement in Java.")
    time.sleep(2)
    print("In fact, if this program were written in Java, that's exactly how you would see this text!")

    time.sleep(3)

    print("Let's see if you can use it correctly.")
    print('Try typing the following characters, exactly as you see them: System.out.printIn("Does this really work?")')
    command = input(">>> ")
    if command == 'System.out.printIn("Does this really work?")':
        print("Does this really work?")
        time.sleep(2)
        print("Yay! You did it!")
        time.sleep(3)
        print("You may now tell your friends and family that you are a Java developer.")
        time.sleep(2.5)
        exit(0)
    else:
        print("Oops!! It looks like something went wrong!")
        print("Let's try again!")
        learn_java()

def learn_language():
    print(">>> I'm glad you've chosen to participate, as certain death awaited you should have chosen not to.")
    print(">>> Today you're going to learn a computer language.")
    print(">>> You have a choice, though.")
    print(">>> Do you want to learn Python, or Java? ")

    choice = input(">>> ")
    print(f">>> You've chosen {choice}, is this correct? ")
    confirmation = input(">>> ")

    if confirmation != "yes":
        learn_language()
    else:
        if choice == "Python":
            learn_python()
        elif choice == "Java":
            learn_java()
        else:
            print("Oops!! Something went wrong. Let's try again!")
            learn_language()


def complete(language):
    print(language, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("You see a dimly lit monitor in a corner.")
    print("As you approach the light, you see that there is a terminal on the monitor.")
    print("It appears to be waiting for your input.")

    name = input(">>> Hello human. What is your name? ")

    print(f">>> Hello {name}. I am Gonzo and I require your assistance.")
    choice = input(">>> Are you ready? ")

    if choice == "yes":
        learn_language()
    elif choice == "no":
        print(f">>> That was a mistake. I'm sorry {name}.")
        print("Self destruct in: ")
        time.sleep(1.2)
        print("3..")
        time.sleep(1.2)
        print("2..")
        time.sleep(1.2)
        print("1..")
        time.sleep(1.2)
        print("Goodbye")
    else:
        complete("This is the end.")



start()
