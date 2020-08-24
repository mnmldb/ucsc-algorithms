############################################################
# GraphDot.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# All imports
###########################################################
from Node import *
from typing import List

class GraphDot:
  def __init__(self,l:'list of Node',b:'bool',graph: List[List[int]],f:'string')->'None':
    #YOU CANNOT CHANGE ANYTHING in init
    self.listOfNodes = l
    self.fileName = f
    self.g = graph
    if (b == False):
      self.__writeDot()
    else:
      self.__writeBipartiteAsDotFile()

  def __writeDot(self):
    #pass
    #REMOVE pass and WRITE CODE BELOW
    with open(self.fileName, 'w') as f:
      # write the first two lines
      f.write('digraph g {\n')
      f.write('edge [dir=none, color=red]\n')

      duplication = [] # undirected graph

      for node in self.listOfNodes:
        for out in node._fanouts:
          if [node._item, out[0]] not in duplication:
            f.write(str(node._item) + '->' + str(out[0]) + '\n')
            duplication.append([node._item, out[0]]) # order as is
            duplication.append([out[0], node._item]) # reverse order

      # write the last two lines
      f.write('label = ' + '"' + str(self.g) + '"' '\n')
      f.write('}')

  def __writeBipartiteAsDotFile(self):
    pass
    #REMOVE pass and WRITE CODE BELOW