# item.py
# CST 205
# Team 7: Cloud 6 Tech         
    
from media import *
	
class item:
  def __init__(self, id, name = '', description = ''):
    self._id = id
    self._name = name
    self._description = description
    
  def getId(self):
    return self._id
    
  def setName(self, name):
    self._name = name
    return
      
  def getName(self):
    return self._name
      
  def setDescription(self, description):
    self._description = description
    return
    
  def getDescription(self):
    return self._description


    
    