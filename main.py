# supposedly start here
import random
import datetime
from math import sqrt
from progressbar import progressbar
greetingID = random.randint(0, 4)
usercmd = input("\nPlease input how do you want to be called\n")
user = usercmd
exit = 0
# Greet the user
print("\nDEBUG_GREET: ", greetingID)
if greetingID == 0:
    print("\n*nom nom nom* Hi!")
elif greetingID == 1:
    print("\nHello there,", user + "!")
elif greetingID == 2:
    print("\nHey there,", user + "!")
elif greetingID == 3:
    print("\nWelcome", user + "!")
else:
    print("\nHi,", user + "!")
# Command loop
while True:
    usercmd = input('\nWhat do you want me to do?\n')
    #if usercmd == "What time it is?":
        #time = datetime.datetime.now()
        #print('It\'s', time)
    #this piece of code is unused because pivin sucks at this
    if usercmd == "Who am I?":
        print("\nYou're", user, "if I'm not mistaken. \n")
    elif usercmd == "Exit":
        print("\nBye", user,"!")
        quit()
    #Quick Menu
    elif usercmd == "Show the Quick Menu":
        print("\nQuick Menu\n")
        print("DOS")
        print("Progressbar95")
        print("Calculator")
        usercmd = input("Return to Sparrow\n")
        if usercmd == "Return to Sparrow":
          print("Returned")
        if usercmd == "DOS":
          exit = 0
          print("\nDOS for Sparrow Assistant\n")
          while exit == 0:
           DOS = input(">")
           if DOS == "exit":
            exit = 1;
        if usercmd == "Progressbar95":
         progressbar()
        elif usercmd == "Calculator":
          #Define all needed numbers then choose the operation
          base = int(input("Type in the first number:\n"))
          additive = int(input("\nType in the second number:\n"))
          operation = input("\nType in the operation (add, substract, multiply, divide, power, square")
          #Do the math based on type of operation
          if operation == "add":
            equality = base + additive
            print(equality)
          elif operation == "substract":
            equality = base - additive
            print(equality)
          elif operation == "multiply":
            equality = base * additive
            print(equality)
          elif operation == "divide":
            equality = base / additive
            print(equality)
          elif operation == "power":
            equality = base ^ additive
            print(equality)
          elif operation == "square":
            #Square root to-do: first ask for operation, omit additive if is square root
            equality = sqrt(base)
            print(equality)
          else:
            print("Invalid operation")
    #About
    elif usercmd == "Who created you?":
        print("\nI was originaly built by pivinx1, but this fork is made by my master setapdede.")
        quit()
    #Quick Menu
    elif usercmd == "Show the Quick Menu":
        print("\nQuick Menu\n")
        usercmd = input("Return to Sparrow\n")
        if usercmd == "Return to Sparrow":
          print("Returned")
    #About
    elif usercmd == "Who created you?":
        print("\nI was originaly built by pivinx1, with contributions from setapdede.")
    elif usercmd == "What is your version?":
        print("\nI see i've got a tech expert here :). I do not have a specific release version but you could say this is 'my first release'.")
    elif usercmd == "Who are you?":
      print("I am an narrow reactive AI codenamed Sparrow, developed by pivinx1, with contributions from setapdede.")
      print("You can call me Sofia though.")
    #Settings
    elif usercmd == "Change my name":
        while usercmd == "Change my name":
         usercmd = input("\nPlease input how do you want to be called\n")
         user = usercmd
    #Jokes
    elif usercmd == "Hey Cortana!":
        print("\nHaha! It surely was funny but I'm not Cortana.")
    elif usercmd == "Ok Google":
        print("\nSorry", user, "but I'm sure I'm not Google's assistant.")
    #Invalid
    else:
        tryID = random.randint(0, 4)
        print("\nI didn't understand what you ment. Could you try rephrasing it?\n")
        if tryID == 0:
          print("(Try 'Who am I?'')")
        if tryID == 1:
          print("(Try 'Who created you?'')")
        if tryID == 2:
          print("(Try 'Hey Cortana!')")
        if tryID == 3:
          print("(Try 'Ok Google')")
        if tryID == 4:
          print("(Try 'What is your version?')")
