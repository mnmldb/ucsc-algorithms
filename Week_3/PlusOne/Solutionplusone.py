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

  # private function
  def _one(self, digit: 'int') -> 'int':
    output = [] # output[0]: new digit, output[1]: True if carry happens
    digit += 1
    if digit == 10:
      output.append(0)
      output.append(True)
    else:
      output.append(digit)
      output.append(False)
    return output 
  
  # plusOne
  def _alg(self, digits: List[int]) -> List[int]:
    n = len(digits)
    iteration = True # set True for the first iteration
    output = []
    for i in range(n):
      if iteration:
        result = self._one(digits[n - i - 1])
        output.insert(0, result[0]) # replace with new digit
        iteration = result[1] # update iteration
      else:
        output.insert(0, digits[n - i - 1])
    if iteration: # plus one
      output.insert(0, 1)
    return output

  # plusOneOnSameList
  def _alg1(self, digits: List[int]) -> 'int':
    digits.insert(0, 0) # insert 0 at the beginning of the list
    n = len(digits)
    iteration = True # set True for the first iteration
    for i in range(n - 1):
      if iteration:
        result = self._one(digits[n - i - 1])
        digits[n - i - 1] = result[0] # replace with new digit
        iteration = result[1] # update iteration
    if iteration: # plus one
      digits[0] = 1 
    if digits[0] == 0:
      del digits[0]

  # convert_to_integer
  def _alg2(self, digits):
    digits = self._alg(digits)
    n = len(digits)
    output = 0
    for i in range(n):
      output += digits[i] * 10 ** (n - i - 1) 
    return output