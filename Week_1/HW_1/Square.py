############################################################
# Square.py
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

class Square():
  def __init__(self):
    self._work  = 0;
    self._u = Util()
    self._testBench()

  
  def _sorted_squares(self, A:List[int]) -> List[int]:
    s = Solution()
    b = s.sortedSquares(A)  # Function to implement
    self._work = s.work_done() ;
    return b
  
  #Private  function
  def _testBench(self):
    self._tests()
    self._testn()
    print("ALL TESTS PASSED")

     
  #Private sunction
  def _test1(self,a:List[int],show:'bool'):
    self ._work  = 0
    n = len(a)
    self._u.assert_ascending(a)
    t1_start = process_time() 
    b = self._sorted_squares(a)
    t1_stop = process_time() 
    d = t1_stop - t1_start; 
    if (show):
      print("--------------------------------------")
      self._u.print_index(n)
      self._u.print_list(a)
      self._u.print_list(b)
    self._u.assert_ascending(b)  
    print("n = ",n, "work =", self ._work , "CPU time in sec =",d)

  #Private sunction
  def _tests(self):
    show = True
    a = [] 
    self._test1(a,show)

    a = [1,2,3]
    self._test1(a,show)

    a = [-2,1]
    self._test1(a,show)

    a = [-3,-2,3]
    self._test1(a,show)

    a = [-4,-1,0,3,10]
    self._test1(a,show)

  #Private sunction
  def _testn(self):
    show = False
    N = 100000 
    for i in range(0,N,1001):
      print("Random tests on Array of size",i)
      a = self._u.generate_random_number(i,False,1,5000)
      a.sort()
      self._test1(a,show)
      



############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing SquareBase.py Starts")
  s = Square()
  print("Testing SquareBase.py Starts")
############################################################
# numCourses up
###########################################################
if (__name__  == '__main__'):
  main()
  
    

