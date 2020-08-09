############################################################
# Util.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
import sys # For getting Python Version
import random 

class Util():
  pass

  ############################################
  # generate_random_number start to end INCLUDED 
  # start to end INCLUDED
  #########################################
  def generate_a_random_number(self,start:int,end:int)->'int':
    v = random.randrange(start,end+1);
    return v

  ############################################
  # generate_random_number GENERATES  N random numbers betweem 
  # start to end INCLUDED
  # if onlypositive is False, generates both pos and negative number
  #  randrange(beg, end, step) :- 
  #  beginning number (included in generation), 
  #  last number (excluded in generation) a
  #  nd step ( to skip numbers in range while selecting).
  #########################################
  def generate_random_number(self, N:int, onlypositive:bool, start:int, end:int)->'List of integer':
    a = []
    for i in range(N):
      v = self.generate_a_random_number(start,end);
      if (onlypositive == False):
        if ((i % 2) == 0): ##//Even. Half are positive, Half are negative
          v = -v ;
      a.append(v)
    return a

  ############################################
  # print_index(10)
  #    0   1   2   3   4   5   6   7   8   9
  #########################################
  def print_index(self, n:int):
    for i in range(n):
      print("{:4d}".format(i),end="")
    print()

  ############################################
  # a = [7,8,9, 23, 100]
  # print_list(a)
  # 7   8   9  23 100
  #########################################
  def print_list(self, a:'list'):
    for i in range(len(a)):
      print("{:4d}".format(a[i]),end="")
    print()

  ############################################
  # a = [7,8,9, 1, 100]
  # crash
  #########################################
  def assert_ascending_range(self, a:'list',start:int, includingend:int):
    t = a[start]
    for i in range(start+1,includingend):
      if (a[i] < t):
        assert(False)

  ############################################
  # a = [7,8,9, 1, 100]
  # crash
  #########################################
  def assert_ascending(self, a:'list'):
    if (len(a)):
      self.assert_ascending_range(a,0,len(a))


  ############################################
  # TEST DRIVERS BELOW
  #########################################
  def _test_random(self,N:int, onlypositive:bool, start:int, end:int)->'None':
    a = self.generate_random_number(N,onlypositive,start,end);
    assert(len(a) == N)
    
  def _test_bed(self):
    self._test_random(10,True,30,100)
    self._test_random(10,False,30,40)
    self.print_index(10)
    a = [7,8,9, 23, 100]
    self.print_list(a)

############################################################
# main 
###########################################################
def main():
	print(sys.version)
	t = Util()
	t._test_bed()
 
  
############################################################
# start up
###########################################################
if (__name__  == '__main__'):
  main()