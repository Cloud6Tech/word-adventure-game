# adventureMain.py
# Team 7: Cloud 6 Tech
# CST 205

setLibPath("D:\\Heather\\Documents\\School\\CSIT\\2015 Fall B - CST 205\\word-adventure-game")
from inputParser import *
from item import *
from player import *
from room import *

def mainFunc():
  #--- --- --- --- --- --- Instantiating Player --- --- --- --- --- ---
  prot = player("prot")
  
  #--- --- --- --- --- --- Instantiating Items --- --- --- --- --- ---
  #Knife may be removed from final build
  #itemKnife = item(1,"knife", "A dull butter knife which looks just perfect for taking on a lion!")
  itemKey = item(2, "Key", "A key which glows bright red.\nIt might fit that lock in the main room!")

  #--- --- --- --- --- --- Instantiating Rooms --- --- --- --- --- ---
  # 1- Entry Room
  roomEntrance = room("Cave Entrance", "A rough hewn cave with a strong stone door at one end, and the entrance to your back")
  
  # 2- Antechamber
  roomAnteChamber = room("Antechamber", "A massive room with finely cut sandstone slabs which adorn the walls, floor and vaulted ceilings") 
  
  # 3- Armory
  roomArmory = room("Armory", "This armory clearly used to be well stocked. Now it's a dusty husk with a table filled with junk and an odd painting on the wall.")
  roomArmory.setInspect("PAINTING","You've found a door hidden behind the painting. You can go North from this room now!")
  
  # 4- Puzzle Room
  roomPuzzle = room("Sphynx Room", "This eerily lit green chamber has a large sphynx in it which eyes you warily")
  
  # 5- Mural Room
  roomMural = room("Mural Room", "This room is dominated by a massive mural depicting frolicking bunnies.\nSomething is scrawled across the face of it.\nMaybe you should look closer.")
  roomMural.setInspect("MURAL","You see the words 'the password is SHUT UP' scrawled across the mural.")
  
  # 6- OldMan Room
  roomOldMan = room("Old Man Room", "In the center of this candlelit room is an old man who looks at you grumpily and hollers 'what's the password?!'")
  
  # 7- Developer's Room
  roomDevelopers = room("Developer Shrine", "This room is dominated by statues with the label 'Glorious Builders' underneath")
  roomDevelopers.setInspect("STATUES","There are 4 statues, each with chiseled features and comically oversized muscles. The names read:\nMatthew Mason - Spinner of Yarns and explorer of Russia\nHeather McCabe - Heroine of the Storm and leader of our company\nJason Lloyd - Slayer of Pythons and master of all things logistical\nBrett Hansen - He's pretty cool too I guess")
  
  # 8- Victory Room
  roomVictory = room("Treasury", "You've made it! You've gotten the treasure and will live out your life with the finest meats and cheeses!")
  
  # 9- Trap Room
  roomTrap = room("Darkness", "You fall into the darkness and are lost. You are likely eaten by a Grue")
   
  #--- --- --- --- --- --- Instantiating Exits & Items --- --- --- --- --- ---
  roomEntrance.setExit("N", roomAnteChamber)
  
  roomAnteChamber.setExit("N", roomVictory)
  roomAnteChamber.setExit("E", roomPuzzle)
  roomAnteChamber.setExit("S", roomEntrance)
  roomAnteChamber.setExit("W", roomArmory)
  
  roomArmory.setExit("S", roomTrap)
  roomArmory.setExit("E", roomAnteChamber)
  #roomArmory.addToInventory(itemKnife)
  
  roomPuzzle.setExit("N", roomOldMan)
  roomPuzzle.setExit("E", roomMural)
  roomPuzzle.setExit("W", roomAnteChamber)
  
  roomMural.setExit("W", roomPuzzle)
  
  roomOldMan.setExit("S",roomPuzzle)
  
  roomDevelopers.setExit("S", roomArmory)
  
  roomVictory.setExit("S", roomAnteChamber)
  
  #--- --- --- --- --- --- Main Code Segment --- --- --- --- --- ---
  #Starting Description
  printNow("You stride boldly into the dank cavern.\nYou come seeking treasure.\nGo forth and find your fortune!\n")
  printNow("(type HELP if you have any questions)\n\n")
  
  #global variable initialization
  victoryFlag = false #This flag will be flipped when player reaches victory room
  keyTaken = false #This flag will be flipped when the key is taken from the oldman after giving him the password
  riddleSolved = false #This flag will be flipped when player solves the Sphynx's riddle
  passwordKey = "SHUT UP" #This is the password scrawled on the mural which the old man needs
  riddleSolution = "LIFE" #Solution to the sphynx's riddle
  currRoom = roomEntrance #currRoom contains current location of player character
  
  #Main loop of program. Will continue to play until the player dies, exits, or reaches victory room
  while(victoryFlag == false):
    #prints current location
    printNow("Current Location: " + currRoom.getName())
    printNow(currRoom.getDescription())
    
    #Checks for special circumstances of victory room, trap room, and puzzle room
    if (currRoom.getName() == roomVictory.getName()):
      printNow("*********************\n*********************\n*********************")
      victoryFlag = true
      break
    elif (currRoom.getName() == roomTrap.getName()):
      break
    elif (currRoom.getName() == roomOldMan.getName() and keyTaken == false):
      printNow("The old man eyes you, expectantly waiting for the password.")
      password = requestString("Enter the password:")
      if (password.upper() == passwordKey):
        printNow("The old man claps his hands with glee and gives you a key!")
        keyTaken = true
        prot.addToInventory(itemKey)
        printNow("========================\n")
        continue
      else:
        printNow("The old man looks at you angrily and screams 'WRONG!' He shoves you out of the room.")
        currRoom = roomPuzzle
        continue
    elif (currRoom.getName() == roomPuzzle.getName() and riddleSolved == false):
      riddleGuess = requestString("The sphynx speaks: 'It has a white light at the end of it and can be over in the blink of an eye. If you have seen our secret, you know it's value. What do I speak of?")
      if (riddleGuess.upper() == riddleSolution):
        printNow("The sphynx narrows its eyes at you for a moment and then announces 'you may pass'")
        riddleSolved = true
        printNow("========================\n")
        continue
      else:
        printNow("The sphynx looks at you angrily and hurls you violently back into the antechamber")
        currRoom = roomAnteChamber
        printNow("========================\n")
        continue
    
    #gets user input for commands
    printNow("What do you do?")
    (cmd, args) = getUserInput()
    
    #Deals with move interaction
    if (cmd == "MOVE"):
      nextRoom = currRoom.getExit(args)
      if (nextRoom == false):
        printNow("I'm sorry, that's not a valid direction")
        printNow("========================\n")
        continue
      elif (nextRoom.getName() == roomVictory.getName() and keyTaken == false):
        printNow("I'm sorry, you don't have the key for that door!")
        printNow("========================\n")
        continue
      else:
        printNow("You boldly move into next room!")
        printNow("========================\n")
        currRoom = nextRoom
        continue
    
    # Handle LOOK command
    elif (cmd == "LOOK"):    
      printNow(currRoom.getLook(args))
      printNow("========================\n")
      continue
      
    # Handle INSPECT command
    elif (cmd == "INSPECT"):
      if (currRoom.getName == roomArmory.getName and args == "PAINTING"):
        roomArmory.setExit("N", roomDevelopers)
      
      printNow(currRoom.getInspect(args))
      printNow("========================\n")
      continue
    
    # Handle TAKE command
    elif (cmd == "TAKE"):
      canTakeItem = currRoom.takeItem(args)
      
      if canTakeItem:
        prot.addToInventory(item)
        printNow("You take the " + args.lower() + ".")
      else:
        printNow("You can't take that.")
      printNow("========================\n")
      continue
     
    #THIS CODE DEALS WITH THE KNIFE WHICH WE MAY BE CUTTING FROM THE GAME, DUE TO IT MAKING THE PUZZLE ROOM TOO BUSY
    #  if (currRoom.getName() == roomArmory.getName()):
    #    if (args == "KNIFE"):
    #      #BROKEN CODE. REVISE PLAYER.SEARCHINVENTORY FUNCTION.
    #      #if (prot.searchInventory(itemKnife) == false ):
    #      prot.addToInventory(itemKnife)
    #      roomArmory.removeFromInventory(itemKnife)
    #      currRoom.removeFromInventory(itemKnife)
    #      printNow("You take the butter knife from the table. Now you're ready to rumble!")
    #      printNow("========================\n")
    #      continue
    #      #else:
    #      #  printNow("I'm sorry, you already have that item!\nPlease try again")
    #      #  printNow("========================\n")
    #      #  continue
    #    else:
    #      printNow("I'm sorry, there's no item like that here.\nPlease try again")
    #      printNow("========================\n")
    #      continue
    #  else:
    #    printNow("I'm sorry, you can't do that here.\nPlease try again")
    #    printNow("========================\n")
    #    continue
      
    #Deals with exit and help requests
    elif (cmd == "MENU"):
      if (args == "EXIT"):
        printNow("A Grue sneaks up from behind and eats you")
        break
      elif (args == "HELP"):
        printNow("Here is your command list:")
        printNow("Move: Lets you move in the cardinal directions. Must be followed by north, south, east or west.\nUsage: move north")
        printNow("Take: In some rooms you may take something. Use with an item name.\nUsage: take banana")
        printNow("Use: will use an item in your inventory. must use with proper item name.\nUsage: use aardvark")
        printNow("Exit: Give up and end your adventure prematurely.\nUsage: exit")
        printNow("Help: will bring up this lovely menu.\nUsage: You really should know this one by now!")
        printNow("========================\n")

    else:
      printNow("I'm sorry, that's not a valid command!\nPlease try again")
      printNow("========================\n")
      continue
  
  #Declares victory or loss upon exit from the while loop.
  if (victoryFlag== true):
    printNow("Get fat upon the fruits of your labor!")
  else:
    printNow("You are a disgrace to adventurers everywhere!\nThis dungeon is saddened by your patheticness!")