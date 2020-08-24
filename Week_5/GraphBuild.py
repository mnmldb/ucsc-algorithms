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
    #WEITE CODE BELOW
    l = len(a)
    empty = 0
    if l: # a is not empty
      e = start + l 
      for i in range(start, e):
        alist = a[i]
        l = len(alist) 
        node = Node(i) # item = i
        for j in alist:
          node._add_fanout(j)
        listOfNodes.append(node)
    return listOfNodes

