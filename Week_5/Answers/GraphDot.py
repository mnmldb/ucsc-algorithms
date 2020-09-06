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
    of = open(self.fileName, 'w')
    of.write('## Jagadeesh Vasudevamurthy ####\n')
    of.write('digraph g {\n')
    of.write('edge [dir=none, color=red]\n')
    for n1 in self.listOfNodes:
      for j in n1.neighbors:
        n2 = self.listOfNodes[j]
        assert(n2.val == j)
        if False or n1.val < n2.val:
          of.write('\t')
          of.write(str(n1.val))
          of.write('->')
          of.write(str(n2.val))
          of.write('\n')
    of.write('\t')
    of.write('label= "')
    of.write(str(self.g))
    of.write('"\n')
    of.write('}\n')
    of.close()

  def __writeBipartiteAsDotFile(self):
    pass
    #REMOVE pass and WRITE CODE BELOW