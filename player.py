# player.py
# Team 7: Cloud 6 Tech
# CST 205

# The player class
# members: name, inventory[], and stats{}

from media import *

class player:
  def __init__(self, name = 'unknown'):
    # Assign the name given to the player
    self._name = name
    # Player created with no items
    self._inventory = []
    # Player starts with no stats
    self._stats = {'life':0, 'str':0, 'dex':0, 'int':0}
  
  # setName() names the player
  def setName(self, name):
    self._name = name
  # getName() returns the name of the player
  def getName(self):
    return self._name
  
  # methods for accessing the stats[] list
  def _setStat(self, key, value):
    self._stats[key] = value
  
  def setLife(self, value):
    self._setStat('life', value)
    
  def setStr(self, value):
    self._setStat('str', value)
  
  def setDex(self, value):
    self._setStat('dex', value)
  
  def setInt(self, value):
    self._setStat('int', value)
    
  def _getStat(self, stat):
    return self._stats[stat]
    
  def getLife(self):
    return self._getStat('life')
    
  def getStr(self):
    return self._getStat('str')
    
  def getDex(self):
    return self._getStat('dex')
    
  def getInt(self):
    return self._getStat('int')
  
  def printStats(self):
    printNow(self._name)
    for i in self._stats.keys():
      printNow( '%s : %s' % (i, self._stats[i]) )
      
  def changeLife(self, value):
    self.setLife( self.getLife() + value )
    return
  
  # methods for accessing the inventory
  
  def printInventory(self):
    for i in self._inventory:
      printNow( i.getDescription() ) 
           
  def addToInventory(self, item):
    self._inventory.append(item)
  
  def searchInventory(self, item):
    for i in range(len(self._inventory)):
      if self._inventory[i].getId() == item:
        return true
      else:
        return false
    
  def removeFromInventory(self, item):
    for i in range(len(self._inventory)):
      if self._inventory[i].id == item.id:
        del self._inventory[i]
        
  def isAlive(self):
    if self.getLife() > 0:
      return true
    else:
      return false