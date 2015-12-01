#  Team Seven: Brett Hansen, Jason Lloyd, Matthew Mason, Heather McCabe
#  CST 205
#  Lab 11/12: Text-based Game
#  inputParser.py

from media import *

def testParser():
  userInput = ""
  
  while userInput != ("MENU","EXIT"):
    userInput = getUserInput()
    printNow("Received input: " + str(userInput))

def getUserInput():

  promptMessage = "What do you do?\n>"
  
  # Prompt for input until input is valid
  while (True):
    inputString = requestString(promptMessage)
      
    # Immediately exit function if the player clicks cancel
    if inputString == None:
      return ("MENU","EXIT")
      
    # Otherwise, process input
    else:
    
      # Handle empty input with reprompt
      if len(inputString) == 0:
        continue
      
      # Capitalize input characters
      inputString = inputString.upper()
      
      # Parse input string on spaces
      command = str.split(inputString)[0]
      args = inputString[len(command)+1:]
      
      # Check for valid "HELP" input; allow full word or just one letter
      if command == "HELP" or command == "H":
        command = "MENU"
        args = "HELP"
        
      # Check for valid "EXIT" input; allow full word or just one letter
      elif command == "EXIT" or command == "X":
        command = "MENU"
        args = "EXIT"        
      
      # Check for valid MOVE/LOOK + directional inputs; allow full word or just one letter
      elif command == "MOVE" or command ==  "LOOK":
        if args == "NORTH" or args == "N":
          args = "NORTH"
        elif args == "SOUTH" or args == "S":
          args = "SOUTH"
        elif args == "EAST" or args == "E":
          args = "EAST"
        elif args == "WEST" or args == "W":
          args = "WEST"
        else: 
          # Reprompt with error message
          promptMessage = "I do not understand where you want to " + command.lower() + ".\n>"
          continue
        
      # Check for valid TAKE/INSPECT/USE input
      elif command == "TAKE" or command == "USE" or command == "INSPECT":
        if len(args) == 0:
          # Reprompt with error message if no item argument is given
          promptMessage = "I do not know what you want to " + command.lower() + ".\n>"
          continue

      # Check for valid DIRECTIONS input; allow the full word or just one letter
      elif command == "DIRECTIONS" or command == "D":
        command = "DIRECTIONS"
        args = "DIRECTIONS"
		  
      # Handle other invalid input with error-message reprompt
      else:
        promptMessage = "I do not understand that.\n>"
        continue
        
      # Return validated input as list (or None if cancel was clicked)
      return (command,args)