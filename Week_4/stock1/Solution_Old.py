############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
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
    ## YoU can have what ever you want
 

  ##Required function to implement
  ##LEETCODE INTERFACE.  DO NOT CHANGE
  ## YOU CANNOT CHANGE ANYTHING
  def maxProfit(self, prices: List[int]) -> int:
    if (False):
      [sellday,buyday,work] = self.nsquare_time_constant_space(prices)
    if (False):
      [sellday,buyday,work] = self.nlogn_time_logn_space(prices)
    if (True):
      [sellday,buyday,work] = self.ntime_constant_space(prices)
    p = self._compute_profit(prices,sellday,buyday)
    return p

  ########################################
  # TIME:THETA(1)
  # Space:THETA(1)
  # I have implemented the code.  NOTHING CAN BE CHANGED HERE
  #########################################
  def _compute_profit(self,a:List[int],s:'int',b:'int') -> 'int':
    n = len(a)
    if (n == 0):
      return 0
    assert(s >= 0 and s < n)
    assert(b >= 0 and b < n)
    assert(s >= b)
    p = a[s] - a[b]
    return p

  ########################################
  # TIME:THETA(N^2)
  # Space:THETA(1)
  # I have implemented the code.  NOTHING CAN BE CHANGED HERE
  #########################################
  def nsquare_time_constant_space(self, a:List[int]) -> '[sellday,buyday,work]':
    n = len(a) 
    gp = 0
    bday = 0
    sday = 0
    work = 0
    for i in range(0,n - 1):
      for j in range(i + 1,n):
        work = work + 1
        p = a[j] - a[i]
        if (p > gp):
          gp = p 
          bday = i 
          sday = j
    return [sday,bday,work]
 
  ########################################
  # Implement your code below
  # You can have any number of private functions and varaible
  #########################################

  ########################################
  # TIME:THETA(NlogN)
  # Space:THETA(logn)
  #########################################
  def nlogn_time_logn_space(self, a:List[int]) -> '[sellday,buyday,work]':
    ##UNTIL YOU IMPLEMENT CALL square_time_constant_space, so that all test passes
    # return self.nsquare_time_constant_space(a)
    n = len(a)
    if n == 1:
        sday = 0
        bday = 0
        work = 1
        return [sday, bday, work]
    else:
        mid = int(round(n/2)) # magic line
        l_stock = a[:mid]
        r_stock = a[mid:]
        
        l_metrics = self.nlogn_time_logn_space(l_stock)
        r_metrics = self.nlogn_time_logn_space(r_stock)
        
        l_sday = l_metrics[0]
        r_sday = r_metrics[0]
        
        l_bday = l_metrics[1]
        r_bday = l_metrics[1]
        
        l_work = l_metrics[2]
        r_work = r_metrics[2]
        
        # l_profit = self._compute_profit(l_stock, l_sday, l_bday)
        # r_profit = self._compute_profit(r_stock, r_sday, r_bday)
        l_profit = l_stock[l_sday] - l_stock[l_bday]
        r_profit = r_stock[r_sday] - r_stock[r_bday]
        c_profit = max(r_stock) - min(l_stock)
        
        c_stock = l_stock + r_stock
        
        slide = len(l_stock) # additional index
        
        if l_profit >= r_profit and l_profit >= c_profit:
            sday = l_sday
            bday = l_bday
        elif r_profit >= l_profit and r_profit >= c_profit:
            sday = r_sday + slide
            bday = r_bday + slide
        else: # c_profit > l_profit and c_profit > r_profit
            sday = r_stock.index(max(r_stock)) + slide
            bday = l_stock.index(min(l_stock))
        
        c_work = len(c_stock) * 2 # find max and min
        work = l_work + r_work + c_work
            
        return [sday, bday, work]

  ########################################
  # TIME:THETA(N)
  # Space:THETA(N)
  #########################################
  def ntime_constant_space(self, a:List[int]) -> '[sellday,buyday,work]':
    ##UNTIL YOU IMPLEMENT CALL square_time_constant_space, so that all test passes
    return self.nsquare_time_constant_space(a)