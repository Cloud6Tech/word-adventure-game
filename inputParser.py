#  Heather McCabe 
#  CST 205
#  Lab 11/12: Text-based Game
#  inputParser.py

def testParser():
  userInput = ""
  
  while userInput != None:
    userInput = getUserInput()
    printNow("Received input: " + str(userInput))

def getUserInput():

  promptMessage = ">"
  
  # Prompt for input until input is valid
  while true:
    userInput = requestString(promptMessage)
      
    # Immediately exit if the player clicks cancel
    if userInput == None:
      printNow("You suddenly burst into flames and die. Bye.")
      return
      
    # Otherwise, process input
    else:
      # Capitalize input characters
      userInput = userInput.upper()
      
      # Handle empty input with normal reprompt
      if userInput == "":
        continue
      
      # Check for valid directional inputs; allow full word or just one letter
      elif userInput == "NORTH" or userInput == "N":
        userInput = "N"
      elif userInput == "SOUTH" or userInput == "S":
        userInput = "S"
      elif userInput == "EAST" or userInput == "E":
        userInput = "E"
      elif userInput == "WEST" or userInput == "W":
        userInput = "W"
        
      # Check for valid "TAKE" input
      elif len(userInput) > 5 and userInput[:5] == "TAKE ":
        # This returns the taken item only; will have to check that item is valid for each room
        userInput = userInput[5:]
        
      # Check for valid "HELP" input
      elif userInput == "HELP" or userInput[0] == "H":
        printNow("Nobody can help you now.")
      
       # Handle invalid input with error-message reprompt
      else:
        promptMessage = "I do not understand that.\n>"
        continue
        
      # Return validated input string (or None if cancel was clicked)
      return userInput