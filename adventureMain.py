# adventureMain.py
# Team 7: Cloud 6 Tech
# CST 205

#setLibPath("C:\\Users\\Bretterbear\\Documents\\GitHub\\word-adventure-game")
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
                 "north, east, or west?") 
  
  # Secret Room
  roomSecret = room("The Pit", "You have found some sort of a hidden room behind the painting; hope begins to build that this could " + \
                    "lead to a way out of this nightmare. After completely entering the room you realize there is no " + \
                    "source of light other than what is bleeding in from the fire behind you. You step to the side to allow more light in " + \
                    "to penetrate the darkness and lose your footing. As you had hoped this room was the end to the nightmare... Just not the " + \
                    "end you were praying for. You have fallen to your death.")
  
  # Knife Room
  roomKnifeBaseDescription = "You immediately notice the warmth of a fire upon your skin as you walk through the door's threshold. " + \
                   "You begin to feel yourself naturally relax as a result of the fire. This quickly dissipates as you take a look around " + \
                   "to see the room is decorated with devices that could serve no other purpose than torture. Directly across from you to " + \
                   "the west, next to the fire, is a single table lined with assorted tools. Looking to the north you notice yet another " + \
                   "door, meaning a continuation to the nightmare."
  roomKnife = room("Torture Chamber", roomKnifeBaseDescription + " To the south nothing immediately catches your eye; however, after a " + \
                   "second look you can't help but notice an elaborate painting of a lovely woman dancing under a pale moon's light.")
                    
  # Developer Credits Room
  roomCredits = room("Developer's Shrine", "In the back wall of the room to the North, you see some sort of strange writing. As you approach, " + \
                     "your heart begins to drop and you feel sick to your stomach as you find that your earlier assumption was correct; you are " + \
                     "part of a sinister game. All is not lost... if this is a game then there must be a way to win!") 
  
  # Bear Room
  roomBearBaseDescription = "Natural light seems for fill this room and you hope this is your exit. You follow the light to find the source is " + \
                            "an opening high in the ceiling, but you see no way to climb up to it."
  roomBear = room("Guardian's Quarters",roomBearBaseDescription + " Directly across from you to the east, you see a door which " + \
                  "appears to be blocked by a monstrous bear. To your relief the animal is asleep, but you will need some sort of weapon to get " + \
                  "past. To the north you spot a small opening which may contain an answer.")  
  
  # Riddle Room
  roomRiddle = room("Prisoner's Cell", "You enter what appears to be a forgotten room. Old spider webs fill the dark crevices and thick carpet of dust " + \
                    "has collected on the stone floor. On the far wall you see an odd plaque with something written on it but you cannot make out " + \
                   "what written from this distance. Perhaps you should take a closer look.")              
 
  # Password Room
  roomPassword = room("Chamber of Whispers", "You finally reach an opening after what seemed to be an eternity traveling through a lightless tunnel. " + \
                      "A soft glow radiates from the center of the room with no obvious cause as to where the source of the light is. You slowly " + \
                      "and very cautiously approach. Once at the soft glow you are able to look at the rest of the room more clearly. " + \
                      "All around the room you see the remains of what appears to be those that have come before for you. Nothing else stands out, " + \
                      "so perhaps you should inspect the light further.")
                  
  # Victory Room
  roomVictoryBaseDescription = "After placing the key in the lock, the door seems to have taken a hold of it on its own. It's as if it has been " + \
                     "waiting for this moment for an eternity, like a hungry animal that has been given a scrap of food."
  roomVictory = room("Exit", roomVictoryBaseDescription + " Speaking of hungry animals, it seems the bear in the next room has awoken. You are not " + \
                     "able to get the door open before the ravenous bear is upon you.")
    
    
  #--- --- --- --- --- --- Add Inspectable Items --- --- --- --- --- --- ---
  # Bear in Guardian's Quarters; inspecting will kill the bear if the player has a knife, creating an East door; also updates victory text
  def bearDoor():
    if prot.searchInventory(1) == true :
      roomBear.setExit("EAST", roomRiddle)
      roomBear.setDescription(roomBearBaseDescription + " To the east, there is the carcass of a bear near a door. " + \
                              "To the north you spot a small opening.")
      roomVictory.setDescription(roomVictoryBaseDescription + " You hear several clicks and slowly the door creeps open. A light so bright " + \
                                 "you have to shield your eyes consumes to blood red glow of the room. Within a couple of seconds you can see " + \
                                 "clearly and walk up long stair case where an open field greets you at the top. You feel the warmth of the " + \
                                 "afternoon sun on your face and realize you have made it out alive.")
      roomBear.setInspect("BEAR","The bear is quite dead.")
  roomBear.setInspect("BEAR","The bear sleeps in front of a door and you cannot go through without disturbing it. You need something to kill it.", bearDoor)
    
  # Knife on table in Torture Room; inspecting gives the player a knife and changes the bear interaction
  def tableKnife():
    if not prot.searchInventory(itemKnife.getId()):
      prot.addToInventory(itemKnife)
      roomKnife.removeInspect("TABLE")
      roomBear.setInspect("BEAR","You remember the knife in your pocket and quickly use it to kill the sleeping bear. The way east is now clear.",bearDoor)
  roomKnife.setInspect("TABLE","At the end of the table you spot a long jagged dagger which could be useful in a dangerous situation. You take it.",tableKnife)
  
  # Painting on wall of Torture Chamber; inspecting creates a South door
  def paintingDoor():
    roomKnife.setExit("SOUTH", roomSecret)
    roomKnife.setDescription(roomKnifeBaseDescription + " To the south, behind an elaborate painting of a lovely woman dancing under a pale moon's light, " + \
                             "there is another door.")
  roomKnife.setInspect("PAINTING","Upon closer examination you see that the painting is wavering ever so slightly. You step a bit closer " + \
                      " and feel a cool breeze and the smell of fresh air. You've found a door hidden behind the painting.",paintingDoor)
                      
  # Inscription on wall in Developer's Shrine
  roomCredits.setInspect("WALL","The wall reads:\nMatthew Mason - Spinner of Yarns and explorer of Russia\n" + \
                         "Heather McCabe - Heroine of the Storm and leader of our company\n" + \
                         "Jason Lloyd - Slayer of Pythons and master of all things logistical\n" + \
                         "Brett Hansen - He's pretty cool too I guess")                    
                      
  # Plaque in Prisoner's Cell; inspecting prompts the player to solve a riddle
  def riddle():
    printNow("The plaque reads: 'It has a white light at the end of it and can be over in the blink of an eye. If you have seen " + \
                        "our secret, you know its value. What do I speak of?")
    riddleGuess = requestString("Speak the answer to the riddle: ")
    if riddleGuess == None: # Cancel
      printNow(">> Unsure, you step away from the plaque.")
      return
    elif riddleGuess.upper() == "LIFE": # Correct answer
      printNow(">> You speak confidently: 'LIFE'")
      printNow("You are suddenly certain that the phrase 'password1234' is important.")
    else: # Incorrect answer
      printNow(">> You speak confidently: '" + riddleGuess.upper() + "'")
      printNow ("Nothing happens. Your answer must have been incorrect.")
  roomRiddle.setInspect("PLAQUE", "", riddle)     
  
  # Light in Chamber of Whispers; inspecting prompts the player to provide the password which will give player a key
  def password():
    printNow("Suddenly, hundreds of voices begin to talk all at the same time. Through the commotion you cannot make out what they are saying. " + \
             "Just before it goes silent you hear a whisper: 'Give us the password to receive our treasure...'")
    passwordGuess = requestString("State the password:")
    if passwordGuess == None: # Cancel
      printNow(">> Unsure, you back away slowly.")
    elif passwordGuess == "password1234": # Correct answer
      prot.addToInventory(itemKey)
      printNow(">> You speak confidently: '" + passwordGuess + "'")
      printNow( "A key suddenly appears in your pocket.")
    else: # Incorrect answer
      printNow(">> You speak confidently: '" + passwordGuess + "'")
      printNow ("The voices shriek: 'Leave us and return when you know the password!'")
  roomPassword.setInspect("LIGHT", "", password)  
  
  
  #--- --- --- --- --- --- Add Initial Exits --- --- --- --- --- ---
  # Empty Room
  roomEntrance.setExit("NORTH", roomChamber)
  
  # Inner Chamber
  roomChamber.setExit("EAST", roomBear)
  roomChamber.setExit("SOUTH", roomEntrance)
  roomChamber.setExit("WEST", roomKnife)
  roomChamber.setExit("NORTH", roomVictory)
  
  # Torture Chamber
  roomKnife.setExit("NORTH", roomCredits)
  roomKnife.setExit("EAST", roomChamber)
  
  # Developer's Shrine
  roomCredits.setExit("SOUTH", roomKnife)
  
  # Guardian's Quarters
  roomBear.setExit("WEST", roomChamber)
  roomBear.setExit("NORTH", roomPassword)
  
  # Chamber of Whispers
  roomPassword.setExit("SOUTH",roomBear)
  
  # Prisoner's Cell
  roomRiddle.setExit("WEST", roomBear)
  
  
  #--- --- --- --- --- --- Add Map Print Function --- --- --- --- ---
  # Get list of room names
  roomList = [roomEntrance.getName(), roomKnife.getName(),roomChamber.getName(),roomBear.getName(), roomRiddle.getName(),
              roomCredits.getName(), roomVictory.getName(),roomPassword.getName()]
  #set flags for rooms visited
  roomFlags = [false, false, false, false, false, false, false, false]  
  
  # Print map of dungeon; [_] indicates visited room, [X] indicates current location
  def printMap():
    # Map lines with northern-most point at level three
    levelOne = ""
    levelTwo = ""
    levelThree = ""
    # Loop through flags list, setting lines to print for all levels
    for key in range(0, len(roomFlags)):
      # Level one is southern-most point and single room set (special case) 
      if key in range(0,1):
        if currRoom.getName() == roomList[key]:
          levelOne = "    [X]"
        elif roomFlags[key] == true:
          levelOne = "    [_]"
      # Level two is comprised of middle rooms
      elif key in range(1, 5):
        if currRoom.getName() == roomList[key]:
          levelTwo += "[X]"
        elif roomFlags[key] == true:
          levelTwo += "[_]"
        else:
          levelTwo += "    "
      # Level three is comprised of northern-most rooms
      elif key in range(5,len(roomFlags)):
         if currRoom.getName() == roomList[key]:
           levelThree += "[X]"
         elif roomFlags[key] == true:
           levelThree += "[_]"
         else:
           levelThree += "    "
    # Print map by line with northern-most point at level three
    printNow("----- MAP -----\n" + levelThree+"\n"+levelTwo+"\n"+levelOne)    
  
  
  #--- --- --- --- --- --- Add Directions Function --- --- --- --- ---
  def getDirections():
    directionString = "You may move in these directions: "
    if (currRoom.getExit("NORTH")!= false):
      directionString = directionString + "[NORTH]  "
    if (currRoom.getExit("EAST")!= false):
      directionString = directionString + "[EAST]  "
    if (currRoom.getExit("SOUTH")!= false):
      directionString = directionString + "[SOUTH]  "
    if (currRoom.getExit("WEST")!= false):
      directionString = directionString + "[WEST]  "
    return directionString
  
  
  #--- --- --- --- --- --- Main Code Segment --- --- --- --- --- ---
  # Global variable initialization
  victoryFlag = false # This flag will be flipped when player reaches victory room
  currRoom = roomEntrance # currRoom contains current location of player character
  
  # Print starting Description
  lineSeparator = "===============================================\n"
  printNow("You awaken from a dream you cannot remember in an unfamiliar setting. As you wait for your eyes to " + \
           "adjust you can't help but notice the pungent sent of decay lingering in the air. You immediately begin " + \
           "to feel a chill running down your spine as the realization hits that you may be part of some sinister game.")
  printNow("(type HELP if you have any questions)\n")
  printNow(lineSeparator)
  printNow("Current Location: " + roomEntrance.getName())
  printMap()
  printNow(roomEntrance.getDescription())
  
  # Main game loop; will loop until the player dies, exits, or reaches victory room
  while(victoryFlag == false):

    # Set victory flag and break if the player is in the victory room
    if (currRoom.getName() == roomVictory.getName() and prot.searchInventory(2) == True):
      # Only win if the bear isn't alive still
      if roomBear.getExit("EAST") != False:
        victoryFlag = True
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
        printNow("That's not a valid direction. " + getDirections())
        continue
      # Victory room is locked
      elif (nextRoom.getName() == roomVictory.getName() and prot.searchInventory(2) == false):
        printNow("You don't have the key for that door.")
        continue
      # Change room, update map and print new description
      else:
        # Set flag for room visited
        for i in range(0,len(roomList)):
          if currRoom.getName() == roomList[i]:
            roomFlags[i] = true
      
        # Print description and map
        printNow(">> You boldly move " + args.lower() + " into the next room.")
        printNow(lineSeparator)
        currRoom = nextRoom
        printNow("Current Location: " + currRoom.getName())
        printMap()
        printNow(currRoom.getDescription())
        continue
    
    # Handle LOOK command (currently disabled)
    #elif (cmd == "LOOK"):    
      #printNow(">> You look to the " + args.lower() + ".")
      #printNow(currRoom.getLook(args))
      #continue
      
    # Handle INSPECT command
    elif (cmd == "INSPECT"):
      printNow(">> You inspect the " + args.lower() + ".")
      inspectDescription = currRoom.getInspect(args)
      if inspectDescription != "":
        printNow(inspectDescription)
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
    
    # Handle DIRECTIONS command
    elif (cmd == "DIRECTIONS"):
      printNow(getDirections())
    
    # Handle EXIT and HELP requests
    elif (cmd == "MENU"):
      if (args == "EXIT"):
        printNow("\nA grue sneaks up from behind and eats you.")
        break
      elif (args == "HELP"):
        printNow("\n# Commands:")
        printNow("# MOVE: Lets you move in the cardinal directions. Must be followed by north, south, east or west. Usage: 'move <direction>'")
        printNow("# INSPECT: Take a closer look at an item. Usage: 'inspect <item>'")
        printNow("# DIRECTIONS: Get a list of room exits. Usage: 'directions'")
        #printNow("# LOOK: Take a closer look in a direction. Usage: 'look <direction>'")
        #printNow("# TAKE: Take an item into your inventory. Usage: 'take <item>'")
        #printNow("# USE: Use an item in your inventory. Usage: 'use <item>'")
        printNow("# EXIT: Give up and end your adventure prematurely. Usage: 'exit'")
        #printNow("# HELP: Bring up this lovely menu. Usage: You really should know this one by now!")
        printNow("\n")
    
    # Handle anything else
    else:
      printNow("That's not a valid command.")
      continue
  
  # Declare victory or loss upon exit from the game loop.
  if (victoryFlag == true): # Win
    printNow("Way to go!")
  else:                     # Loss
    printNow("You are a disgrace to adventurers everywhere!\nThis dungeon is saddened by your patheticness!")