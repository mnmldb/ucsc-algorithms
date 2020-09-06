############################################################
# Graph.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# YOU CAN CHANGE THIS LINE BELOW
###########################################################
# outputDir = "C:\\scratch\\outputs\\dot\\"
outputDir = '/Users/dn/Documents/UCSC/Week_6/Dot_Files/'

############################################################
#          YOU CANNOT CHANGE ANYHING BELOW
###########################################################

###########################################################
from typing import List

## from typing import List ONLY FOR DOUMENTAION #################
#### The Python runtime does not enforce function 
#and variable type annotations. 
#They can be used by third party tools such as type checkers, IDEs, linters, etc
## https://docs.python.org/3/library/typing.html
#############################################


############################################################
# All imports
###########################################################
from Node import *
from GraphBuild import *
from GraphDot import *
from GraphBipartite import *

class Graph:
  def __init__(self):
    self._testBench();

  def buildGraph(self,start:'int',a:'list of list')->'list of Nodes':
    t = GraphBuild();
    return t.getListOfNodes(start,a)

  def dotGraph(self,a:'list of nodes',fileName:'string')->'None':
    GraphDot(firstNode,fileName);

  def BipartiteGraph(self,a:'list of nodes',start:'int',fin:'string',fout:'string') -> bool:
    f1 = outputDir + fin
    f2 = outputDir + fout
    t = GraphBipartite(start,f1,f2) ;
    return t.isBipartite(a)

  def _testBench(self):
    if (False):
      self._testBuild();

    if (True):
      self._testBipartite()
 

  def _test1Build(self,a: List[List[int]],start:'int',fin:'string'):
    print("--------Working on Graph ", a,"----------");
    t = GraphBuild();
    listOfNodes = t.getListOfNodes(start,a)
    if (listOfNodes == None):
      return 
    l = len(listOfNodes)
    if (l):
      GraphDot(listOfNodes,False,a,outputDir + fin);
      print("Dot file is at",outputDir + fin)


  def _test1Bipartite(self,a: List[List[int]],start:'int',expectedAns:'bool',fin:'string',fout:'string') -> bool:
    print("--------Working on Graph ", a,"----------");
    t = self.BipartiteGraph(a,start,fin,fout)
    if (t == expectedAns):
        if (t == True):
          print("Graph is Bipartite")
          print("Bipartite Graph is in ",outputDir +fout)
        else:
          print("Graph is NOT Bipartite")
    else:
        if (expectedAns == True):
          print("Graph is Bipartite. But you are telling NOT Bipartite")
        else:
          print("Graph is NOT Bipartite. But you are telling Bipartite")
        assert(False)  

  def _testBuild(self):
    start = 0
    a = [[1,3], [0,2], [1,3], [0,2]]
    self._test1Build(a,start,"b1in.dot")

    start = 0
    a = [[1,2,3], [0,2], [0,1,3], [0,2]]
    self._test1Build(a,start,"b2in.dot")

    start = 0
    a = [[3,5], [4,5], [5], [0],[1],[1,2]]
    self._test1Build(a,start,"b3in.dot")

    start = 0
    a = [[4,5,6], [4,5], [5,6], [5],[0,1],[2,3],[0,2]]
    self._test1Build(a,start,"b4in.dot")

    start = 0
    a = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    self._test1Build(a,start,"b5in.dot")

    start = 0
    a = [[],[3],[],[1],[]]
    self._test1Build(a,start,"b6in.dot")

    start = 0
    a = [[1], [0], [3], [2]]
    self._test1Build(a,start,"b7in.dot")

    start = 0
    a = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
    self._test1Build(a,start,"b8in.dot")

    print("------------ ALL BUILD TESTS PASSED -------------")
    print("---------  Make one doc that has all the figures. DO NOT ATTACH DOT FILES")

  def _testBipartite(self):
    start = 0
    a = [[1,3], [0,2], [1,3], [0,2]]
    ea = True
    self._test1Bipartite(a,start,ea,"b1in.dot","b1out.dot")

    start = 0
    a = [[1,2,3], [0,2], [0,1,3], [0,2]]
    ea = False
    self._test1Bipartite(a,start,ea,"b2in.dot","b2out.dot")

    start = 0
    a = [[3,5], [4,5], [5], [0],[1],[1,2]]
    ea = True
    self._test1Bipartite(a,start,ea,"b3in.dot","b3out.dot")

    start = 0
    a = [[4,5,6], [4,5], [5,6], [5],[0,1],[2,3],[0,2]]
    ea = True
    self._test1Bipartite(a,start,ea,"b4in.dot","b4out.dot")

    start = 0
    a = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    ea = False
    self._test1Bipartite(a,start,ea,"b5in.dot","b5out.dot")

    start = 0
    a = [[],[3],[],[1],[]]
    ea = True
    self._test1Bipartite(a,start,ea,"b6in.dot","b6out.dot")

    start = 0
    a = [[1], [0], [3], [2]]
    ea = True
    self._test1Bipartite(a,start,ea,"b7in.dot","b7out.dot")

    start = 0
    a = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
    ea = False
    self._test1Bipartite(a,start,ea,"b8in.dot","b8out.dot")

    print("------------ ALL Bipartite test passed PASSED -------------")

############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  t = Graph()
############################################################
# start up
###########################################################
if (__name__  == '__main__'):
  main()