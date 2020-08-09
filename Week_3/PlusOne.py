############################################################
# PlusOne.py
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

class PlusOne():
  def __init__(self):
    self._u = Util()
    self._test_bench()

  def _plus_one(self, digits: List[int]) -> List[int]:
    s = Solution()
    b = s.plusOne(digits)  # Function to implement
    return b

  def _plus_one_on_same_list(self, digits: List[int]):
    s = Solution()
    s.plusOneOnSameList(digits)  # Function to implement

  def _check(self, a: List[int], b: List[int], v:'int')->'bool':
    s = Solution()
    x = s.convert_to_integer(a) # Function to implement
    y = s.convert_to_integer(b) 
    if (y == (x + v)):
      return True
    return False

  def _test_bench(self):
    self._tests()
    self._testn()
    print("ALL TESTS PASSED")

  def _test1(self,a:List[int],show:'bool'):
    self._work  = 0
    b = self._plus_one(a)
    f = self._check(a,b,1)
    if (show or (f == False)):
      self._u.print_list(a)
      self._u.print_list(b)
    assert(f == True)

    self._plus_one_on_same_list(a)
    f = self._check(a,b,0) #b is already a+1
    if (show or (f == False)):
      self._u.print_list(a)
      self._u.print_list(b)
    assert(f == True)
    if (show):
      print("--------------------------------------")
 
  def _tests(self):
    show = True
    a = [1, 2, 3]
    self._test1(a,show)

    a = [1, 7, 8, 9]
    self._test1(a,show)

    a = [9, 9]
    self._test1(a,show)

  def _testn(self):
    show = False
    N = 100000 
    print(N, "tests start",N)
    for i in range(N):
      a = []
      if (i == 0):
        a.append(i)
      else:
        while (i != 0):
          a.append(i % 10)
          i = i //10
      self._test1(a,show)
    print(N, "tests passed")
      

############################################################
# main 
###########################################################
def main():
  print("Testing PlusOneBase.py Starts")
  s = PlusOne()
  print("Testing PlusOneBase.py Starts")
############################################################
#Caller
###########################################################
if (__name__  == '__main__'):
  main()
  
    

