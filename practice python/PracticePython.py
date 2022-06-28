import random

def CharacterInput():
    name = input("What is your name?:\n")
    ageTrue = True
    while ageTrue == True:
        age = input("What is your age:\n")
        try:
            age = int(age)
            ageTrue = False
        except:
            print("You did not enter a number\nTry again")
    print(f"{name}, you will be 100 years old in {100-age} years")

def OddOrEven():
    numTrue1 = True
    while numTrue1 == True:
        num1 = input("Pick the first number:\n")
        try:
            num1 = int(num1)
            numTrue1 = False
        except:
            print("You did not enter a number\nTry Again")
            
    numTrue2 = True
    while numTrue2 == True:
        num2 = input("Pick the second number:\n")
        try:
            num2 = int(num2)
            numTrue2 = False
        except:
            print("You did not enter a number\nTry Again")
            
    if num1 % 2 == 0: 
        print(f"{num1} is a even number")
    else:
        print(f"{num1} is not a even number")
    
    if num1 % 4 == 0:
        print(f"{num1} is divisible by 4")
    else:
        print(f"{num1} is not divisible by 4")
    
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}")
    else: 
        print(f"{num1} is not divisible by {num2}")

def listLessThanTen():
    randomlist = random.sample(range(1, 50), 10)
    
    print(f"The list:\n{randomlist}\n")
    
    returnList1 = []
    for x in randomlist:
        if x <= 5:
            returnList1.append(x)
    
    print(f"numbers tht are lower than 5 are\n{returnList1}\n")
    
    checkTrue = True
    while checkTrue == True:
        check = input("Pick a number to see all the numbers below in the list:\n")
        try:
            check = int(check)
            checkTrue = False
        except:
            print("You did not enter a number\nTry Again")
    
        returnList2 = []
    for x in randomlist:
        if x <= check:
            returnList2.append(x)
    
    print(f"\nThe numbers lower than {check} in the list are\n{returnList2}\n")

def divisor():
    numTrue = True
    num = True
    while numTrue == True:
        num = input("Pick a number:\n")
        try:
            num = int(num)
            numTrue = False
        except:
            print("You did not enter a number\nTry Again")
    
    list = range(1, 1000)
    returnList = []
    for x in list:
        if x % num == 0:
            returnList.append(x)
        else: pass
    
    print(f"Numbers that are divisible by {num} are \n{returnList}")

def listOverlap():
    a = random.sample(range(1, 50), 10)
    b = random.sample(range(1, 50), 10)
    returnList = []
    for x in a:
        for y in b:
            if x == y:
                if x in returnList:
                    pass
                else:
                    returnList.append(x)
    print(a)
    print(b)
    print(returnList)

def stringList():
    wordTrue = True
    while wordTrue == True:
        word = input("Pick a word:\n")
        try:
            if len(word) > 1:
                wordTrue = False
        except:
            print("You entered one letter\nTry Again")
    listReversed = []
    for c in reversed(word):
        listReversed.append(c)
    listrev = ''
    for x in listReversed:
        listrev += x
    
    if word == listrev:
        print(f"'{word}' is palindrome")
    else: print(f"'{word}' is not palindrome")

def listComprehensions():
    randomlist = random.sample(range(1, 50), 20)
    
    list = []
    for x in randomlist:
        if x % 2 == 0:
            list.append(x)
    
    print(f"The list is:\n{randomlist}\nThe even numbers are \n{list}")

def rockPaperScissors():
    playAgain = True
    while playAgain == True:
        userInputTrue = True
        while userInputTrue == True:
            userInput = input("Pick, Rock Paper or Scissors:\n")
            userInput = userInput.lower()

            if userInput == "rock" or userInput == "r":
                userInputConfirmation = "rock"
                userInputTrue = False
            elif userInput == "scissors" or userInput == "s":
                userInputConfirmation = "scissors"
                userInputTrue = False
            elif userInput == "paper" or userInput == "p":
                userInputConfirmation = "paper"
                userInputTrue = False
            else:
                print("You did not choose from\nRock Paper or Scissors\nTry Again")
            
        aiNum = random.randint(1, 3)
        if aiNum == 1:
            ai = "rock"
        elif aiNum == 2:
            ai = "paper"
        else:
            ai = "scissors"
        
        if userInput == ai:
            print(f"You picked {userInput}\nAI chose {ai}\nIt is a tie go again")
        elif userInput == "rock" and ai == "paper":
            print(f"You picked {userInput}\nAI chose {ai}\nYou Lose")
            repeatLoop = True
            while repeatLoop == True:
                repeat = input('Do you want to play again?\n')
                repeat = repeat.lower()
                if repeat == "yes" or repeat == "y":
                    playAgain = True
                    repeatLoop = False
                elif repeat == "no" or repeat == "n":
                    repeatTrue = False
                    repeatLoop = False
                    playAgain = False
                else:
                    print("you did not pick from yes or no\nTry again")
        elif userInput == "rock" and ai == "scissors":
            print(f"You picked {userInput}\nAI chose {ai}\nYou Win")
            repeatLoop = True
            while repeatLoop == True:
                repeat = input('Do you want to play again?\n')
                repeat = repeat.lower()
                if repeat == "yes" or repeat == "y":
                    playAgain = True
                    repeatLoop = False
                elif repeat == "no" or repeat == "n":
                    repeatTrue = False
                    repeatLoop = False
                    playAgain = False
                else:
                    print("you did not pick from yes or no\nTry again")     

        elif userInputConfirmation == "paper" and ai == "scissors":
            print(f"You picked {userInputConfirmation}\nAI chose {ai}\nYou Lose")
            repeatLoop = True
            while repeatLoop == True:
                repeat = input('Do you want to play again?\n')
                repeat = repeat.lower()
                if repeat == "yes" or repeat == "y":
                    playAgain = True
                    repeatLoop = False
                elif repeat == "no" or repeat == "n":
                    repeatTrue = False
                    repeatLoop = False
                    playAgain = False
                else:
                    print("you did not pick from yes or no\nTry again")
        elif userInputConfirmation == "paper" and ai == "rock":
            print(f"You picked {userInputConfirmation}\nAI chose {ai}\nYou Win")
            repeatLoop = True
            while repeatLoop == True:
                repeat = input('Do you want to play again?\n')
                repeat = repeat.lower()
                if repeat == "yes" or repeat == "y":
                    playAgain = True
                    repeatLoop = False
                elif repeat == "no" or repeat == "n":
                    repeatTrue = False
                    repeatLoop = False
                    playAgain = False
                else:
                    print("you did not pick from yes or no\nTry again")   

        elif userInputConfirmation == "scissors" and ai == "rock":
            print(f"You picked {userInputConfirmation}\nAI chose {ai}\nYou Lose")
            repeatLoop = True
            while repeatLoop == True:
                repeat = input('Do you want to play again?\n')
                repeat = repeat.lower()
                if repeat == "yes" or repeat == "y":
                    playAgain = True
                    repeatLoop = False
                elif repeat == "no" or repeat == "n":
                    repeatTrue = False
                    repeatLoop = False
                    playAgain = False
                else:
                    print("you did not pick from yes or no\nTry again")
        elif userInputConfirmation == "scissors" and ai == "paper":
            print(f"You picked {userInputConfirmation}\nAI chose {ai}\nYou Win")
            repeatLoop = True
            while repeatLoop == True:
                repeat = input('Do you want to play again?\n')
                repeat = repeat.lower()
                if repeat == "yes" or repeat == "y":
                    playAgain = True
                    repeatLoop = False
                elif repeat == "no" or repeat == "n":
                    repeatTrue = False
                    repeatLoop = False
                    playAgain = False
                else:
                    print("you did not pick from yes or no\nTry again")
        if playAgain == False:
            print("GoodBye")

rockPaperScissors()
