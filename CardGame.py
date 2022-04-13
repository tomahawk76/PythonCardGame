import pyinputplus as pyinp

def cardGame():
    blackCards = 13
    for cards in range(1, 14, 1):
        if blackCards > 0:
            myTaken = pyinp.inputInt("How many do you want to take? ", min=1, max=3)
            blackCards -= myTaken
            print(f"You took {myTaken} cards. There are {blackCards} black cards left.")
            aiTaken = 4 - myTaken
            if blackCards - aiTaken > 0:
                blackCards -= aiTaken
                print(f"The AI took {aiTaken} cards. There are {blackCards} black cards left.\n")  
                        
        if blackCards == 1:
            myTaken = pyinp.inputInt("How many do you want to take? ", min=1, max=1)
            blackCards -= myTaken
            print(f"You took {myTaken} cards. There are {blackCards} black cards left.\n")

        if blackCards == 2:
            myTaken = pyinp.inputInt("How many do you want to take? ", min=1, max=2)
            blackCards -= myTaken
            print(f"You took {myTaken} cards. There are {blackCards} black cards left.\n")

        if blackCards == 0:
            print("The AI took the red card! They win!\n")
            break

cardGame()
