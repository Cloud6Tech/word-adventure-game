# adventureMain.py
# Team 7: Cloud 6 Tech
# CST 205

setLibPath("D:\\Heather\\Documents\\School\\CSIT\\2015 Fall B - CST 205\\word-adventure-game")
#setLibPath("C:\\Users\\masonm\\CST205\\word_game\\word-adventure-game")
from inputParser import *
from item import *
from player import *
from room import *


def mainFunc():
  #--- --- --- --- --- --- Instantiating Player --- --- --- --- --- ---
  prot = player("prot")
  
  #--- --- --- --- --- --- Instantiating Items --- --- --- --- --- ---
  #Knife may be removed from final build
  itemKnife = item(1,"Knife", "A long jagged knife stained with blood from previous uses!")
  itemKey = item(2,"Key","A key which glows bright red.\nIt might fit that lock in the main room!")


  #--- --- --- --- --- --- Instantiating Rooms --- --- --- --- --- ---
  # Entrance
  roomEntrance = room("Empty Room","To the north you spot a decrepit door sitting in the pale light of a dying torch. " + \
                      "As you approach, the smell of decay intensifies and you can't help but fear what may be waiting " + \
                      "for you on the other side. With no other exits in sight, do you choose to move forward?")
  
  # Inner Chamber
  roomChamber = room("Inner Chamber", "Upon entering the room the smell of decaying flesh burns through your nose and fills your " + \
                 "lungs like a fire consuming a house. In the center of the room stands a single lamp, giving off an eerie " + \
                 "red glow. The lamp appears to cast living shadows upon the walls. As you cautiously approach the light you " + \
                 "can't help but notice a faint thump getting louder as the lamp gets closer. Upon reaching the lamp you realize " + \
                 "the cause of the thumping sound is liquid dripping on to the lamp. You reach and touch the lamp only to " + \
                 "increased your own dread; the lamp is soaked in blood. With your heart pounding you take swift look around and " + \
                 "notice there are three doors, all leading in opposite directions. Which door do you choose to open first: " + \
                 "North, East, or West?") 
  
  # Secret Room
  roomSecret = room("The Pit", "You have found some sort of a hidden room behind the painting; hope begins to build that this could " + \
                    "lead to a way out of this nightmare. After completely entering the room you realize there is no " + \
                    "source of light other than what is bleeding in from the fire behind you. You step to the side to allow more light in " + \
                    "to penetrate the darkness and lose your footing. As you had hoped this room was the end to the nightmare... Just not the " + \
                    "end you were praying for. You have fallen to your death.")
  
  # Knife Room
  roomKnife = room("Torture Chamber", "You immediately notice the warmth of a fire upon your skin as you walk through the door's threshold. " + \
                   "You begin to feel yourself naturally relax as a result of the fire. This quickly dissipates as you take a look around " + \
                   "to see the room is decorated with devices that could serve no other purpose than torture. Directly across from you to " + \
                   "the West, next to the fire, is a single table lined with assorted tools. Looking to North you notice yet another " + \
                   "door, meaning a continuation to the nightmare. To the South nothing immediately catches your eye, however, after a " + \
                   "second look you can't help but notice an elaborate painting of a lovely woman dancing under a pale moon's light.")
                    
  # Developer Credits Room
  roomCredits = room("Developer's Shrine", "In the back wall of the room to the North, you see some sort of strange writing. As you approach, " + \
                     "your heart begins to drop and you feel sick to your stomach as you find that your earlier assumption was correct; you are " + \
                     "part of a sinister game. All is not lost... if this is a game then there must be a way to win!") 
  
  # Bear Room
  roomBear = room("Guardian's Quarters","Natural light seems for fill this room and you hope this is your exit. You follow the light to find the source is " + \
                  "an opening high in the ceiling, but you see no way to climb up to it. Directly across from you to the East, you see a door which " + \
                  "appears to be blocked by a monstrous bear. To your relief the animal is asleep, you will need some sort of weapon to get " + \
                  "past. To the North you spot a small opening which may contain an answer. How do you wish to proceed?")  
  
  # Riddle Room
  roomRiddle = room("Prisoner's Cell", "You enter what appears to be a forgotten room. Old spider webs fill the dark crevices and thick carpet of dust " + \
                    "has collected on the stone floor. On the far wall you see an odd plaque with something written on it but you cannot make out " + \
                   "what written from this distance. Perhaps you should take a closer look.")              
 
  # Password Room
  roomPassword = room("Chamber of Whispers", "You finally reach an opening after what seemed to be an eternity travelling through a lightless tunnel. " + \
                      "A soft glow radiates from the center of the room with no obvious cause as to where the source of the light is you slowly " + \
                      "and very cautiously approach. Once at the soft glow you are able to look at the rest of the room more clearly. " + \
                      "All around the room you see the remains of what appears to be those that have come before for you. Nothing else stands out, perhaps you should inspect the light further")
                  
  # Victory Room
  roomVictory = room("Exit", "After placing the key in the lock, the door seems to have taken a hold of it on its own. It?s as if it has been " + \
                     "waiting for this moment for an eternity, like a hungry animal that has been given a scrap of food. You hear several clicks " + \
                     "and slowly the door creeps open. A light so bright you have to shield your eyes consumes to blood red glow of the room. " + \
                     "Within a couple of seconds you can see clearly and walk up long stair case where an open field greets you at the top." +\
                     " You feel the warmth of the afternoon sun of you face and realize you have made it out alive.")
    
  #--- --- --- --- --- --- Add Inspectable Items --- --- --- --- --- --- ---
  # Knife on table in Torture Room; inspecting gives the player a knife
  def tableKnife():
    if not prot.searchInventory(itemKnife.getId()):
      prot.addToInventory(itemKnife)
      roomKnife.removeInspect("TABLE")
  roomKnife.setInspect("TABLE","At the end of the table you spot a long jagged dagger which could be useful in a dangerous situation. You take it.",tableKnife)
  
  # Painting on wall of Torture Chamber; inspecting creates a South door
  def paintingDoor():
    roomKnife.setExit("S", roomSecret)
  roomKnife.setInspect("PAINTING","Upon closer examination you see that the painting is wavering ever so slightly. You step a bit closer " + \
                      " and feel a cool breeze and the smell of fresh air. You've found a door hidden behind the painting.",paintingDoor)
                      
  # Inscription on wall in Developer's Shrine
  roomCredits.setInspect("WALL","The wall reads:\nMatthew Mason - Spinner of Yarns and explorer of Russia\n" + \
                         "Heather McCabe - Heroine of the Storm and leader of our company\n" + \
                         "Jason Lloyd - Slayer of Pythons and master of all things logistical\n" + \
                         "Brett Hansen - He's pretty cool too I guess")                    
                      
  # Bear in Guardian's Quarters; inspecting will kill the bear if the player has a knife
  def bearDoor():
    if prot.searchInventory(1) == true :
      roomBear.setExit("E", roomRiddle)
      printNow ("You have killed the sleeping bear with the knife. The way east is now clear.")
      return "You have killed the sleeping bear with the knife. The way east is now clear."
  roomBear.setInspect("BEAR","A bear sleeps in front of a door and you cannot go through without disturbing it. You need something to kill it.", bearDoor)
  
  # Plaque in Prisoner's Cell; inspecting prompts the player to solve a riddle
  def riddle():
    riddleGuess = requestString("Speak the answer to the riddle: ")
    if riddleGuess.upper() == "LIFE":
      printNow( "Here's the passwordddddddddddddddd. password1234")
      return "Here's the passwordddddddddddddddd. password1234"
    else:
      printNow ("That is incorrect. Comeback when you are ready to try again")
      return "Nothing happens."
  roomRiddle.setInspect("PLAQUE", "The plaque reads: 'It has a white light at the end of it and can be over in the blink of an eye. If you have seen " + \
                        "our secret, you know its value. What do I speak of?'",riddle)     
  
  # Light in Chamber of Whispers; inspecting prompts the player to provide the password which will give player a key
  def password():
    passwordGuess = requestString("You state the password aloud:")
    if passwordGuess == "password1234":
      #prot.addToInventory(itemKey)
      printNow( "A key suddenly appears in your pocket.")
      passwordFlag = true
    else:
      printNow ("Leave us and return when you know the password!")
      prot.addToInventory(itemKey)
  roomPassword.setInspect("LIGHT", "Suddenly, hundreds of voices begin to talk all at the same time. Through the commotion you cannot make out what they are saying. " + \
                         "Just before it goes silent you hear a whisper: 'Give us the password to receive our treasure..",password)  
  
  #--- --- --- --- --- --- Add Initial Exits --- --- --- --- --- ---
  roomEntrance.setExit("NORTH", roomChamber)
  
  roomChamber.setExit("EAST", roomBear)
  roomChamber.setExit("SOUTH", roomEntrance)
  roomChamber.setExit("WEST", roomKnife)
  roomChamber.setExit("NORTH", roomVictory)
  
  roomKnife.setExit("NORTH", roomCredits)
  roomKnife.setExit("EAST", roomChamber)
  
  roomCredits.setExit("SOUTH", roomKnife)
  
  roomBear.setExit("WEST", roomChamber)
  roomBear.setExit("NORTH", roomPassword)
  
  roomPassword.setExit("SOUTH",roomBear)
    
  roomRiddle.setExit("WEST", roomBear)
  
  #--- --- --- --- --- --- Main Code Segment --- --- --- --- --- ---
  #Starting Description
  lineSeparator = "========================\n"
  printNow("You awaken from a dream you cannot remember in an unfamiliar setting. As you wait for your eyes to " + \
           "adjust you can't help but notice the pungent sent of decay lingering in the air. You immediately begin " + \
           "to feel a chill running down your spine as the realization hits that you may be part of some sinister game.")
  printNow("(type HELP if you have any questions)\n")
  printNow(lineSeparator)
  printNow("Current Location: " + roomEntrance.getName())
  printNow(roomEntrance.getDescription())
 
  
  #global variable initialization
  victoryFlag = false #This flag will be flipped when player reaches victory room
  currRoom = roomEntrance #currRoom contains current location of player character
  
  #Main loop of program. Will continue to play until the player dies, exits, or reaches victory room
  while(victoryFlag == false):
    
    # Set victory flag and break if the player is in the victory room
    if (currRoom.getName() == roomVictory.getName()):
      victoryFlag = true
      break
    # Break if the player is in the secret room
    elif (currRoom.getName() == roomSecret.getName()):
      break
    
    # Get player command input
    (cmd, args) = getUserInput()
    
    # Handle MOVE command
    if (cmd == "MOVE"):
      nextRoom = currRoom.getExit(args)
      # Invalid direction/no room in that direction
      if (nextRoom == false):
        printNow("That's not a valid direction.")
        continue
      # Victory room is locked
      elif (nextRoom.getName() == roomVictory.getName() and prot.searchInventory(2) == false):
        printNow("You don't have the key for that door.")
        continue
      # Change room, print new description
      else:
        printNow(">> You boldly move " + args.lower() + " into the next room.")
        printNow(lineSeparator)
        currRoom = nextRoom
        printNow("Current Location: " + currRoom.getName())
        printNow(currRoom.getDescription())
        continue
    
    # Handle LOOK command
    elif (cmd == "LOOK"):    
      printNow(">> You look to the " + args.lower() + ".")
      printNow(currRoom.getLook(args))
      continue
      
    # Handle INSPECT command
    elif (cmd == "INSPECT"):
      printNow(">> You inspect the " + args.lower() + ".")
      printNow(currRoom.getInspect(args))
      continue
    
    # Handle TAKE command
    elif (cmd == "TAKE"):
      canTakeItem = currRoom.takeItem(args)
      
      if canTakeItem:
        prot.addToInventory(item)
        printNow(">> You take the " + args.lower() + ".")
      else:
        printNow("You can't take that.")
      continue
     
    # Handle EXIT and HELP requests
    elif (cmd == "MENU"):
      if (args == "EXIT"):
        printNow("A Grue sneaks up from behind and eats you.")
        break
      elif (args == "HELP"):
        printNow(lineSeparator)
        printNow("Here is your command list:")
        printNow("Move: Lets you move in the cardinal directions. Must be followed by north, south, east or west.\nUsage: move north")
        printNow("Take: In some rooms you may take something. Use with an item name.\nUsage: take banana")
        printNow("Use: will use an item in your inventory. must use with proper item name.\nUsage: use aardvark")
        printNow("Exit: Give up and end your adventure prematurely.\nUsage: exit")
        printNow("Help: will bring up this lovely menu.\nUsage: You really should know this one by now!")
        printNow(lineSeparator)

    else:
      printNow("That's not a valid command.")
      continue
  
  #Declares victory or loss upon exit from the while loop.
  if (victoryFlag== true):
    printNow("Way to go!")
  else:
    printNow("You are a disgrace to adventurers everywhere!\nThis dungeon is saddened by your patheticness!")