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
    ## YOU CANNOT ADD ANTHING HERE
    pass

  ##Required function to implement
  def hop_easy(self, A:List[int],f:'int') -> 'int':
    ## NOTHING CAN BE CHANGED HERE
    return self._hop_easy(A,f)

  ##Required function to implement
  def hop(self, A:List[int],f:'int') -> 'int':
    ## NOTHING CAN BE CHANGED HERE
    return self._hop(A,f)

  ########################################
  # TIME:THETA(N)
  # Space:THETA(1)
  # I have implemented the code. NOTHING CAN BE CHANGED HERE
  #########################################
  def _hop_easy(self, a:List[int],f:'int') -> 'int':
    ## n = len(a)  ##YOU CANNOT CALL len
    t = f
    h = 0
    while (True):
      if (a[t] == f):
        return h 
      else:
        t = a[t]
        h = h + 1
    return h

  ##Implement your code
  '''
   *  YOU CANNOT CHANGE INTERFACE OF THIS ROUTINE
	 *  YOU CANNOT USE ANY static variable in this function
	 *  YOU can use many local variables inside the function
	 *  Cannot use any loop statements like:  for, while, do, while, go to
	 *  Can use if
	 *  ONLY AFTER THE execution of this routine LIST a MUST have the same contents as you got it.
	 *  YOU cannot call any subroutine inside this function except _hop itself 
	 *  If your code is more than 10 lines, you don't understand the problem
	 '''
  ########################################
  # TIME:FILL
  # Space:FILL
  #########################################
  def _hop(self, a:List[int],f:'int') -> 'int':
    ## n = len(a)  ##YOU CANNOT CALL len
    print("WRITE CODE NOW ONLY THIS PROCEDURE")
    if a[f] == f:
      return 0
    else:
      nf = a[f]
      a[f] = a[nf]
      l = 1 + self._hop(a, f)
      a[f] = nf
      return l
