############################################################
# Square.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################
############################################################
# All imports
###########################################################
from typing import List


class Solution:
  def __init__(self):
    self._work = 0

  ##Required function to implement
  def sortedSquares(self, A:List[int]) -> List[int]:
    ## NOTHING CAN BE CHANGED HERE
    return self._alg(A)

  def work_done(self) -> 'int':
    ## NOTHING CAN BE CHANGED HERE
    return self._work 

  ##Implement your code
  ##You can have any number of private variables and functions
  def _alg(self, A:List[int]) -> List[int]:
    self._work = len(A)
    return sorted(list(map(lambda x: x ** 2, A)))

  '''
  Time Limit Exceeded 1: Bubble Sort
  def _alg(self, A:List[int]) -> List[int]:
      n = len(A) # number of integers
      B = list(map(lambda x: x ** 2, A)) # square
      switch = True
      while switch:
          switch = False
          for i in range(0, n - 1):
              if B[i] > B[i + 1]:
              B[i], B[i + 1] = B[i + 1], B[i]
              switch = True
      return B
  '''
  
  '''
  Time Limit Exceeded 2: Count Sort
  def _alg(self, A:List[int]) -> List[int]:
      B = list(map(lambda x: x ** 2, A)) # square
      n_min = min(B)
      n_max = max(B)
      n = n_max - n_min + 1 # bin
      C = [0] * n
      for i in B:
          C[i - n_min] += 1
      D = [i for i, j in enumerate(C, start=n_min) for _ in range(j)]
      return D
  '''
