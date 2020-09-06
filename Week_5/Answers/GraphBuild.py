############################################################
# GraphBuild.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# All imports
###########################################################
from Node import *

############################################################
# You must write code to build a graph
###########################################################
class GraphBuild:
  def __init__(self):
    pass

  def getListOfNodes(self, start:'int',a:'list of list')->'list of Node':
    listOfNodes = []
    l = len(a)
    empty = 0
    if l:
      e = start + l 
      for i in range(start, e):
        alist = a[i]
        l = len(alist) 
        if l:
          empty = empty + 1
        # even the length is 0 we make a node
        n = Node(i, Node.GREEN, alist)
        listOfNodes.append(n)
      if empty == 0: # e.g. [[], [], []]
        return None
      return listOfNodes
    else:
      return None

