# room.py
# CST 205
# Team 7: Cloud 6 Tech

# Defines the class room
# Each room has:
# a name 
# a description
# an inventory of items
# a list of exits

from media import *

class room:
  def __init__(self, name = '' , description = ''):
    self._name = name
    self._description = description
    # Each room starts without inspectable items
    self._inspect = {}
    # Each room starts without lookable directions
    self._look = {}
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
  
  # setLook() sets the description of a certain direction in the room
  def setLook(self,direction,description):
    self._look[direction] = description

  # getLook() returns the description of a certain direction in the room
  def getLook(self,direction):
    if direction in self._look:
      return self._look[direction]
    else:
      return "There is nothing of interest in that direction."

  # addToInventory() adds an item to _inventory[]
  def addToInventory(self, item):
    self._inventory.append(item)
    return
    
  # printInventory() prints every item in _inventory[]  
  def printInventory(self):
    for i in self._inventory:
      printNow(i.description)
    
  # takeItem() removes an item identified by name from the inventory[]
  # Returns true if item was found, false if not
  def takeItem(self,itemName):
    for item in self._inventory:
      if item.getName().upper() == itemName:
        self._inventory.remove(item)
        return True
    return False
  
  # removeFromInventory() removes an item from the inventory[]
  def removeFromInventory(self, item):
    # go through each item in inventory
    for i in range(len(self._inventory)):
      # search for the item by ID
      if self._inventory[i].getId == item.getId:
        # remove the item from the list
        del self._inventory[i]
  
  # setInspect() sets the description of an item that can be inspected
  def setInspect(self,item,description):
    self._inspect[item] = description

  # getInspect() returns the description of an item that can be inspected
  def getInspect(self,item):
    if item in self._inspect:
      return self._inspect[item]
    else:
      return "That is nothing of interest."

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