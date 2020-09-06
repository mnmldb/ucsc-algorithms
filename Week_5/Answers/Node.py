############################################################
# Node.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################


class Node:
  #Remove pass
  #DEFINE your data structure here
  ##YOU CAN add whatever you want
  GREEN = 1
  RED = 2
  BLUE = 3
  def __init__(self, val = 0, color = GREEN, neighbors = None):
    self.val = val
    self.color = color
    self.neighbors = neighbors if neighbors is not None else [] # equal to fanouts
  def setColor(self, c):
    self.color = c
  
  def getColor(self) -> 'color':
    return self.color
  
  def colorAllNodes(self, l:'list of Node', c:'color'):
    for n in l:
      n.setColor(c)
  
  def GetFirstNodeThatHasColor(self, l:'list of Node', c:'color') -> 'Node':
    for n in l:
      if n.getColor() == c:
        return n
    return None
