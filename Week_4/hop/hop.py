############################################################
# Hop.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
#           NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
from typing import List
from Util import *
from time import process_time 
from Solution import *

class Hop():
  def __init__(self):
    self._show = False
    self._u = Util()
    self._testBench()

  def _hop_easy(self, a:List[int],f:'int') -> 'int':
    s = Solution()
    b = s.hop_easy(a,f)  # Function to implement
    return b

  def _hop(self, a:List[int],f:'int') -> 'int':
    s = Solution()
    b = s.hop_easy(a,f)  # Function to implement
    return b
  
  #Private  function
  def _testBench(self):
    self._tests()
    self._testn()
    print("ALL TESTS PASSED")

     
  #Private sunction
  def _test1(self,a:List[int],f:'int'):
    b = a.copy()
    n = len(a)
    h1 = self._hop_easy(a,f)
    if (a != b):
      print("Array content changed after hop_easy")
      assert(False)
    h2 = self._hop(a,f)
    if (a != b):
      print("Array content changed after hop")
      assert(False)
    if (h1 != h2):
      print("Expected hop length =",h1, "But your length = ",h2)
      assert(False)
    if (self._show):
      n = len(a)
      print("-------Looking for",f,"------------------")
      self._u.print_index(n)
      self._u.print_list(a)     
      print("Num hopped:", h2)

  #Private sunction
  def _tests(self):
    self._show = True
    s = [5,1,0,4,2,3] 
    self._test1(s,3)

    for i in s:
      self._test1(s,i)


  #Private sunction
  def _testn(self):
    self._show = False
    n = 10000
    a = self._u.generate_suffled_number_between_1_to_n(n)
    print("----------",n,"tests------------")
    for i in a:
      self._test1(a,i)
    print("All",n, "Tests are passed. You are a genius")
      

############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing Hop.py Starts")
  s = Hop()
  print("Testing Hop.py Ends")
  print("Upload only Solution.py and output of the program as shown above")
  print("For A all tests must pass")

############################################################
# numCourses up
###########################################################
if (__name__  == '__main__'):
  main()
  
    

