############################################################
# Friends.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
#           NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
from Util import *
from Solution import *

class Friends():
  def __init__(self):
    self._u = Util()
    self._testBench()

  def _friends(self, n:'int'):
    ans = [0,0]
    s = Solution(n,ans)
    s.friends()  # Function to implement
    return ans
  
  def _testBench(self):
    self._tests()
    print("ALL TESTS PASSED")

  def _test1(self,n:'int'):
    print("-------------", n , "-------------------------")
    t1_start = process_time()
    a = self._friends(n)
    t1_stop = process_time() 
    d = t1_stop - t1_start; 
    print(n, " has ", a[0], " friends. Took", a[1], " steps to compute")
    print("Total CPU time in sec =",d)
    logn_base2 = self._u.log_lower_bound(n,2)
    nlogn = n * logn_base2
    w = a[1] / nlogn 
    print("n = ", n)
    print("logn ", logn_base2)
    print("nlogn ",nlogn)
    print("constant term  with nlogn", w)


  def _tests(self):
    n = 10000
    a = self._test1(n)

    n = 20000
    a = self._test1(n)

    n = 100000000 ## YOU CANNOT CHANGE THIS. This must pass for A
    a = self._test1(n)


############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing Friends.py Starts")
  s = Friends()
  print("Testing Friends.py ENDS")
############################################################
# numCourses up
###########################################################
if (__name__  == '__main__'):
  main()