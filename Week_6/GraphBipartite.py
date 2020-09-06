############################################################
# GraphBipartite.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# All imports
###########################################################

###########################################################
from typing import List

## from typing import List ONLY FOR DOUMENTAION #################
#### The Python runtime does not enforce function 
#and variable type annotations. 
#They can be used by third party tools such as type checkers, IDEs, linters, etc
## https://docs.python.org/3/library/typing.html
#############################################
from GraphBuild import *
from GraphDot import *
from Node import *

class GraphBipartite:
  def __init__(self, start:'int',fin:'string',fout:'string'):
    self.start = start
    self.fin = fin 
    self.fout = fout
    ##YOU CAN ADD WHATEVER YOU WANT BELOW


  ## KEEP same interface as Leetcode
  def isBipartite(self, graph: List[List[int]]) -> bool:
    ## YOU CANNOT CHANGE anything below
    return self.__alg(graph)
    
  def __alg(self, graph: List[List[int]]) -> bool:
    ## YOU CANNOT CHANGE anything in _alg
    t = GraphBuild();
    listOfNodes = t.getListOfNodes(self.start,graph)
    if (listOfNodes == None):
      return True
    l = len(listOfNodes)
    if (l):
      GraphDot(listOfNodes,False,graph,self.fin);
      print("Original Graph is in ",self.fin)
      b = self.__isBipartite(listOfNodes)
      if (b):
        GraphDot(listOfNodes,True,graph,self.fout);
        print("Bipartite Graph is in ",self.fout)
      return b
    else:
      return True

  ##   WRITE CODE BELOW ################
  ##  You can have as many number of private functions and private variables #########
  def __isBipartite(self,listOfNodes:'list of Node') -> bool:
    #pass
    #REMOVE PASS AND WRITE CODE

    #Color each node to GREEN
    t = Node()
    t.colorAllNodes(listOfNodes, Node.GREEN)
    while True:
      n = t.GetFirstNodeThatHasColor(listOfNodes, Node.GREEN) #need this to deal with unliked graph
      if n:
        b = self._isBipartiteBFS(n, listOfNodes)
        if b == False:
          return False
      else:
        ##Graph is Bipatite
        return True
  
  def _isBipartiteBFS(self, n:'Node', listOfNodes:'list of Node') -> bool:
    q = [] #queue of nodes
    assert(n.getColor() == Node.GREEN)
    #GREEN is not visited
    #If the graph is bipartite, all nodes should be colored in RED or BLUE
    n.setColor(Node.RED)
    q.append(n) #set in the queue
    while len(q) != 0: #loop will end when the queue is empty
      n = q.pop() #remove from the queue
      ncolor = n.getColor()
      assert(ncolor != Node.GREEN)
      #ncolor will either RED or BLUE
      oppositeColorofN = Node.RED
      if ncolor == Node.RED:
        oppositeColorofN = Node.BLUE
      ##Can go on each fanout of n
      for j in n.neighbors:
        f = listOfNodes[j]
        fcolor = f.getColor()
        if fcolor == Node.GREEN:
          #f NOT visited
          f.setColor(oppositeColorofN)
          q.append(f) #set in the queue
        else:
          if fcolor == ncolor:
            return False




