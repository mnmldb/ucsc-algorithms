############################################################
# LookAndSay.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
from Solution import *

class LookAndSay():
  def __init__(self):
    self._testBench()

  def _look_and_say_integer(self,n:'int')->'string':
    s = Solution()
    return s.countAndSay(n) #implement in solution

  def _look_and_say_string(self,n:'string')->'string': 
    s = Solution()
    return s.countAndSayString(n) #implement in solution

  #private function
  def _testBench(self):
    self._tests()
    self._testn()
    print("ALL TESTS PASSED")
     

  #Private sunction
  def _tests(self):
    n = "123" 
    e = "111213" 
    s = self._look_and_say_string(n) 
    assert(s == e);

    n = "9999999999" 
    e = "109" 
    s = self._look_and_say_string(n) 
    assert(s == e);

    n = "9876543210" 
    e = "19181716151413121110" 
    s = self._look_and_say_string(n) 
    assert(s == e);

  #Private sunction
  def _testn(self):
    n = 1 
    e = "1" 
    s = self._look_and_say_integer(n) 
    assert(s == e);

    n = 2 
    e = "11" 
    s = self._look_and_say_integer(n) 
    assert(s == e);

    n = 3
    e = "21" 
    s = self._look_and_say_integer(n) 
    assert(s == e);

    n = 4 
    e = "1211" 
    s = self._look_and_say_integer(n) 
    assert(s == e);

    n = 5
    e = "111221" 
    s = self._look_and_say_integer(n) 
    assert(s == e);

    for n in range(1,32):
      s = self._look_and_say_integer(n)
      print("n = ",n, " Length = ", len(s))
      print("n = ",n," ",s)

############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  t = LookAndSay()
############################################################
# start up
###########################################################
if (__name__  == '__main__'):
  main()   

