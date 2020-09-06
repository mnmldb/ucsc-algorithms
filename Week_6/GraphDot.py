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
    #pass
    #REMOVE pass and WRITE CODE BELOW
    of = open(self.fileName, 'w')
    of.write('## Jagadeesh Vasudevamurthy ####\n')
    of.write('graph g {\n')
    of.write('\toverlap=false; splines=true\n')
    of.write('\tedge [style=dotted, weight=10, len=.2]\n')
    of.write('\tsubgraph cluster_RED {\n')
    of.write('''\t\tRED [pos="-1,0!", color=red /* , style=invis */]\n''')
    #WRITE ALL RED NODES
    for n in self.listOfNodes:
      c = n.getColor()
      assert(c == Node.RED or c == Node.BLUE)
      if c == Node.RED:
        of.write('\t\t')
        of.write(str(n.val))
        of.write(' -- RED\n')
    of.write('\t}\n')
    of.write('\tsubgraph cluster_BLUE {\n')
    of.write('''\t\tRED [pos="-1,0!", color=blue /* , style=invis */]\n''')
    #WRITE ALL BLUE NODES
    for n in self.listOfNodes:
      c = n.getColor()
      assert(c == Node.RED or c == Node.BLUE)
      if c == Node.BLUE:
        of.write('\t\t')
        of.write(str(n.val))
        of.write(' -- BLUE\n')
    of.write('\t}\n')
    of.write('\tedge [style="", weight=1, len=1]\n')

    for n in self.listOfNodes:
      c = n.getColor()
      if c == Node.RED:
        ##WRITE RED CONNECTIONS
        ##Can go on each fanout of n
        for j in n.neighbors:
          f = self.listOfNodes[j]
          if n.val < f.val:
            of.write('\t')
            of.write(str(n.val))
            of.write('--')
            of.write(str(f.val))
            of.write('\n')
      elif c == Node.BLUE:
        ##WRITE BLUE CONNECTIONS
        ##Can go on each fanout of n
        for j in n.neighbors:
          f = self.listOfNodes[j]
          if n.val < f.val:
            of.write('\t')
            of.write(str(n.val))
            of.write('--')
            of.write(str(f.val))
            of.write('\n')
    of.write('\t')
    of.write('label= "')
    of.write(str(self.g))
    of.write('"\n')
    of.write('}\n')
    of.close()
