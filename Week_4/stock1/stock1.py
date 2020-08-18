############################################################
# Stock1.py
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

class Stock1():
  def __init__(self):
    self._show = False
    self._u = Util()
    self._testBench()

  def _nsquare_time_constant_space(self, a:List[int])->'[sellday,buyday,work]':
    s = Solution()
    return s.nsquare_time_constant_space(a)  # Function to implement

  def _nlogn_time_logn_space(self, a:List[int])->'[sellday,buyday,work]':
    s = Solution()
    return s.nlogn_time_logn_space(a)  # Function to implement

  def _ntime_constant_space(self, a:List[int])->'[sellday,buyday,work]':
    s = Solution()
    return s.ntime_constant_space(a)  # Function to implement
    

  def _testBench(self):
    self._tests()
    self._testn()
    print("ALL TESTS PASSED")

     
  def _test1(self,a:List[int]):
    n = len(a)
    if (self._show):
      self._u.print_index(n)
      self._u.print_list(a)

    [sellday1,buyday1,work1] = self._nsquare_time_constant_space(a)
    p1 = self._compute_profit(a,sellday1,buyday1)
    if (self._show):
      print("nsquare_time_constant_space", "work =", work1, "Profit =",p1)

    [sellday2,buyday2,work2] = self._nlogn_time_logn_space(a)
    p2 = self._compute_profit(a,sellday2,buyday2)
    if (self._show):
      print("nlogn_time_nlogn_space", "work =", work2, "Profit =",p2)

    if (p1 != p2):
      print("Why profits are different",p1,p2)
      assert(p1 == p2)

    [sellday3,buyday3,work3] = self._ntime_constant_space(a)
    p3 = self._compute_profit(a,sellday3,buyday3)
    if (self._show):
      print("nlogn_time_nlogn_space", "work =", work3, "Profit =",p3)

    if (p1 != p3):
      print("Why profits are different",p1,p3)
      assert(p1 == p3)
    return [work1,work2,work3]
 
  def _compute_profit(self,a:List[int],s:'int',b:'int')->'int':
    n = len(a)
    if (n == 0):
      return 0
    assert(s >= 0 and s < n)
    assert(b >= 0 and b < n)
    assert(s >= b)
    p = a[s] - a[b]
    return p

  def _tests(self):
    self._show = True
    s = [5, 10, 4, 6, 12] 
    self._test1(s)

    s = [7,1,5,3,6,4]
    self._test1(s)

  def _testn(self):
    self._show = False
    n = 100

    print("----------",n," ascending tests------------")
    a = self._u.generate_n_numbers_in_ascending_order(n)
    work = self._test1(a)
    print("nsquare_time_constant_space work", work[0])
    print("nlogn_time_nlogn_space work", work[1])
    print("nl_time_constant_space work", work[2])
    print("ascending tests passed")

    print("----------",n," descending tests------------")
    a = self._u.generate_n_numbers_in_ascending_order(n)
    work = self._test1(a)
    print("nsquare_time_constant_space work", work[0])
    print("nlogn_time_nlogn_space work", work[1])
    print("nl_time_constant_space work", work[2])
    print("descending tests passed")

    print("----------",n," same value tests------------")
    a = self._u.generate_n_same_k_number(n,7)
    work = self._test1(a)
    print("nsquare_time_constant_space work", work[0])
    print("nlogn_time_nlogn_space work", work[1])
    print("nl_time_constant_space work", work[2])
    print("same value tests passed")

    n = 500
    print("----------",n," random tests------------")
    work = [0,0,0]
    for i in range(n):
      a = self._u.generate_random_number(n,False,1,101)
      w = self._test1(a)
      work[0] = work[0] + w[0]
      work[1] = work[1] + w[1]
      work[2] = work[2] + w[2]
    print("nsquare_time_constant_space work", work[0])
    print("nlogn_time_nlogn_space work ", work[1])
    print("nl_time_constant_space work", work[2])
    print("All",n, "Random tests passed. You are a guru in stock trading")
      

############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing Stock1.py Starts")
  s = Stock1()
  print("Testing Stock1.py Ends")
  print("Upload only Solution.py and output of the program as shown above")
  print("For A all tests must pass")

############################################################
# numCourses up
###########################################################
if (__name__  == '__main__'):
  main()
  
    

