############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################
############################################################
# All imports
###########################################################
from typing import List

class Solution:
  def __init__(self):
    pass

  ##Required function to implement
  def plusOne(self, digits: List[int]) -> List[int]:
    ## NOTHING CAN BE CHANGED HERE
    return self._alg(digits)

  def plusOneOnSameList(self, digits: List[int]):
    ## NOTHING CAN BE CHANGED HERE
    return self._alg1(digits)

  def convert_to_integer(self,digits: List[int]) -> 'int':
    ## NOTHING CAN BE CHANGED HERE
    return self._alg2(digits)

  ##Implement your code
  ##You can have any number of private variables and functions