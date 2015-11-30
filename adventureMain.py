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
  itemKnife = item(1,"Knife", "A dull butter knife which looks just perfect for taking on a lion!")
  itemKey = item(2, "Key", "A key which glows bright red.\nIt might fit that lock in the main room!")

  #--- --- --- --- --- --- Instantiating Rooms --- --- --- --- --- ---
  # Entrance
  roomEntrance = room("Entrance", "To the north sitting in the pale light of a dying torch you spot a decrepit door. " + \
                      "As you approach, the smell of decay intensifies and you can't help but fear what may be waiting " + \
                      "for you on the other side. With no other exits in sight, do you choose to move forward?")
  
  # Red Room
  roomRed = room("Red Room", "Upon entering the room the smell of decaying flesh burns through your nose and fills your " + \
                 "lungs like a fire consuming a house. In the center of the room stands a single lamp, giving off an eerie " + \
                 "red glow, which appears to cast living shadows upon the walls. As you cautiously approach the light you " + \
                 "can?t help but notice a faint thump getting louder as the lamp gets closer. Upon reaching the lamp you realize " + \
                 "the cause of the thumping sound is liquid dripping on to the lamp. You reach and touch the lamp only to " + \
                 "increased your own dread; the lamp is soaked in blood. With your heart pounding you take swift look around and " + \
                 "notice there are three doors, all leading in opposite directions. Which door do you choose to open first: " + \
                 "North, East, or West?") 
  
  # Secret Room
  roomSecret = room("Secret Room", "You have found some sort of a hidden room behind the painting; hope begins to build that this could " + \
                    "lead to a way out of the nightmare you have awoken to. After completely entering the room you realize there is no " + \
                    "source of light other than what is bleeding in from the fire behind you. You step to the side to allow more light in " + \
                    "to penetrate the darkness and lose your footing. As you had hoped this room was the end to the nightmare... Just not the " + \
                    "end you were praying for. You have fallen to your death.")
  
  # Knife Room
  roomKnife = room("Knife Room", "You immediately notice the warmth of a fire upon you skin as you walk through the door?s threshold. " + \
                   "You begin to feel yourself naturally relax as a result of the fire. This quickly dissipates as you take a look around " + \
                   "to see the room is decorated with devices that could serve no other purpose than torture. Directly across from you to " + \
                   "the West, standing next to the fire, is a single table lined with assorted tools. Looking to North you notice yet another " + \
                   "door meaning the continuation of this nightmare. To the South nothing immediately catches your eye, however, after a " + \
                   "second look you can't help but notice an elaborate painting of a lovely woman dancing under a pale moon's light.")
  roomKnife.setInspect("TABLE","There is a knife! You take it.",prot.addToInventory,[itemKnife])
  def paintingDoor():
      roomKnife.setExit("S", roomSecret)
  roomKnife.setInspect("PAINTING","You've found a door hidden behind the painting.",paintingDoor)
                    
  # Developer Credits Room
  roomCredits = room("Developer's Shrine", "In the back wall of the room to the North, you see some sort of strange writing. As you approach, " + \
                     "your heart begins to drop and you feel sick to your stomach as you find that your earlier assumption was correct: you are " + \
                     "part of a sinister game. All is not lost... if this is a game then there must be a way to win!")
  roomCredits.setInspect("WALL","The wall reads:\nMatthew Mason - Spinner of Yarns and explorer of Russia\n" + \
                         "Heather McCabe - Heroine of the Storm and leader of our company\n" + \
                         "Jason Lloyd - Slayer of Pythons and master of all things logistical\n" + \
                         "Brett Hansen - He's pretty cool too I guess")
  
  # Bear Room
  roomBear = room("Bear Room","Natural light seems for fill this room and you hope this is your exit. You follow the light to find the source is " + \
                  "an opening high in the ceiling, but you see no way to climb up to it. Directly across from you to the East, you see a door which " + \
                  "appears to be blocked by a monstrous bear. To your relief the animal seem to be asleep, you will need some sort of weapon to get " + \
                  "past. To the North you spot a small opening which may contain an answer. How do you wish to proceed?")
  
  
  # Riddle Room
  roomRiddle = room("Riddle Room", "You enter what appears to be a forgotten room. Old spider webs fill the dark crevices and thick carpet of dust " + \
                    "has collected on the stone floor. On the far wall you see an odd plaque with something written on it but you cannot make out " + \
                    "what it says from this distance. Perhaps you should take a closer look.")              
  def riddle():
    riddleGuess = requestString("Speak the answer to the riddle: ")
    if riddleGuess.upper() == "LIFE":
      return "Here's the passwordddddddddddddddd"
    else:
      return "Nothing happens."
  roomRiddle.setInspect("PLAQUE", "The plaque reads: 'It has a white light at the end of it and can be over in the blink of an eye. If you have seen " + \
                        "our secret, you know its value. What do I speak of?",riddle)      
  
  
  # Password Room
  roomPassword = room("Password Room", "You finally reach an opening after what seemed to be an eternity travelling through a lightless tunnel. " + \
                      "A soft glow radiates from the center of the room with no obvious cause as to where the source of the light is you slowly " + \
                      "and very cautiously approach. Once at the soft glow you are able to look at the rest of the room more clearly. " + \
                      "All around the room you see the remains of what appears to be those that have come before for you.")
  def password():
    passwordGuess = requestString("Suddenly, hundreds of voices begin to talk all at the same time but through the commotion you cannot make " + \
                                  "out what they are saying. Finally, just before it goes silent you hear: 'Give us the password to move on.' You " + \
                                  "state the password aloud:")
    if passwordGuess == "password1234":
      prot.addToInventory(itemKey)
      return "A key suddenly appears in your pocket."
    else:
      return "Nothing happens."
  roomPassword.setSpecial(password)
  
  # Victory Room
  roomVictory = room("Exit", "After placing the key in the lock, the door seems to have taken a hold of it on its own. It?s as if it has been " + \
                     "waiting for this moment for an eternity, like a hungry animal that has been given a scrap of food. You hear several clicks " + \
                     "and slowly the door creeps open. A light so bright you have to shield your eyes consumes to blood red glow of the room. After a " + \
                     "couple of seconds you can see clearly and step out into and open field where you feel the warmth of the afternoon sun of you face. " + \
                     "You have made it out alive.")
    
  #--- --- --- --- --- --- Instantiating Initial Exits --- --- --- --- --- ---
  roomEntrance.setExit("N", roomRed)
  
  roomRed.setExit("E", roomBear)
  roomRed.setExit("S", roomEntrance)
  roomRed.setExit("W", roomKnife)
  
  roomKnife.setExit("N", roomCredits)
  roomKnife.setExit("E", roomRed)
  
  roomCredits.setExit("S", roomKnife)
  
  roomBear.setExit("W", roomRed)
  roomBear.setExit("N", roomPassword)
  
  roomPassword.setExit("S",roomBear)
    
  roomRiddle.setExit("W", roomBear)
  
  #--- --- --- --- --- --- Main Code Segment --- --- --- --- --- ---
  #Starting Description
  printNow("You awaken from a dream you cannot remember in an unfamiliar setting. As you wait for your eyes to " + \
           "adjust you can?t help but notice the pungent sent of decay lingering in the air. You immediately begin " + \
           "to feel a chill running down your spine as the realization hits that you may be part of some sinister game.")
  printNow("(type HELP if you have any questions)\n\n")
  
  #global variable initialization
  victoryFlag = false #This flag will be flipped when player reaches victory room
  currRoom = roomEntrance #currRoom contains current location of player character
  
  #Main loop of program. Will continue to play until the player dies, exits, or reaches victory room
  while(victoryFlag == false):
    #prints current location
    printNow("Current Location: " + currRoom.getName())
    printNow(currRoom.getDescription())
    
    #Checks for special circumstances of victory room, trap room, and puzzle room
    currRoom.runSpecial()
    if (currRoom.getName() == roomVictory.getName()):
      printNow("*********************\n*********************\n*********************")
      victoryFlag = true
      break
    elif (currRoom.getName() == roomSecret.getName()):
      break
    
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