# room.py
# CST 205
# Team 7: Cloud 6 Tech

# Defines the class room
# Each room has:
# a name 
# a description
# an inventory of items
# a list of exits
class room:
  def __init__(self, name = '' , description = ''):
    self._name = name
    self._description = description
    # Each item starts without any items
    self._inventory = []
    # Each room starts with no exits
    self._exits = {}
    # Initializing the special function 
    self._special = ()
    
  # setSpecial() stores the special function in this room
  def setSpecial(self, function):
    self._special = function
    return
  
  # runSpecial() runs the stored special function  
  def runSpecial(self):
    self._special()  
  
  # setName() sets the name of the room
  def setName(self, name):
    self._name = name
    return
  
  # getName() returns the name of the room
  def getName(self):
    return self._name
  
  # setDescription() sets the description of the room
  def setDescription(self, description):
    self._description = description
    return
  
  # getDescription() returns the description of the room
  def getDescription(self):
    return self._description
  
  # addToInventory() adds an item to _inventory[]
  def addToInventory(self, item):
    self._inventory.append(item)
    return
    
  # printInventory() prints every item in _inventory[]  
  def printInventory(self):
    for i in self._inventory:
      printNow(i.description)
  
  # removeFromInventory() removes an item from the inventory[]
  def removeFromInventory(self, item):
    # go through each item in inventory
    for i in range(len(self._inventory)):
      # search for the item by ID
      if self._inventory[i].getId == item.getId:
        # remove the item from the list
        del self._inventory[i]
  
  # setExit() adds an entry in _exits by it's direction
  # direction is a string, room should be another room object
  def setExit(self, direction, room):
    self._exits[direction] = room
  
  # delExit() deletes an exit from the room
  def delExit(self, direction):
    # If the direction is in _exits{}, delete it
    if direction in self._exits.keys():
      del self._exits[direction]
      
  # getExit() returns the room object that cooresponds with each direction
  # Will return false if there is no room in that direction
  def getExit(self, direction):
    if direction in self._exits.keys() and self._exits[direction]:
      return self._exits[direction]
    else:
      return false