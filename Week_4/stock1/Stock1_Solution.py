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
    ## YoU can have what ever you want
    self._min = 1
    self._max = 2

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
    n = len(a)
    if n == 0:
      return 0
    work = [0]
    return self._dq(a, 0, n - 1, work)


  def _get_min_or_max_index(self, a:List[int], s:'int', m:'int', work:'list of size 1', minormax:'int') -> 'int':
    v = a[s]
    vi = s
    for i in range(s + 1, m + 1):
      work[0] = work[0] + 1
      if minormax == self._min:
        if a[i] < v:
          v = a[i]
          vi = i
      else:
        if a[i] > v:
          v = a[i]
          vi = i
    return vi # return index


  def _dq(self, a:List[int], l:'int', h:'int', work:'list of size 1') -> '[sellday, buyday, work]':
    if l == h:
      # exactly one element
      # Profit is zero
      ans = [h, l, work[0]]
      return ans
    
    # Divide
    work[0] = work[0] + 1
    m = ((h - l) // 2) + l 
    #Left side profit index
    li = self._dq(a, l, m, work) # li = sellday, buyday, work
    #Right side profit index
    ri = self._dq(a, m + 1, h, work) # li = sellday, buyday, work

    # Conquer
    work[0] = work[0] + 1

    # Find minimum number index on left side
    minlefti = self._get_min_or_max_index(a, l, m, work, self._min)
    maxrighti = self._get_min_or_max_index(a, m + 1, h, work, self._max)

    crossprofit = self._compute_profit(a, maxrighti, minlefti)
    leftprofit = self._compute_profit(a, li[0], li[1])
    rightprofit = self._compute_profit(a, ri[0], ri[1])

    # First figure out left or right is profitable
    leftrightprofitindex = li # sellday, buyday, work
    leftrightprofit = leftprofit
    if rightprofit > leftprofit:
      leftrightprofitindex = ri # sellday, buyday, work
      leftrightprofit = rightprofit
    
    ## Now compare with cross profit
    if crossprofit > leftrightprofit:
      ans = [maxrighti, minlefti, work[0]]
      return ans
    else:
      ans = [leftrightprofitindex[0], leftrightprofitindex[1], work[0]]
      return ans

  ########################################
  # TIME:THETA(N)
  # Space:THETA(N)
  #########################################
  def ntime_constant_space(self, a:List[int]) -> '[sellday,buyday,work]':
    ##UNTIL YOU IMPLEMENT CALL square_time_constant_space, so that all test passes
    n = len(a)
    if n == 0:
      return [0, 0, 0]
    work = 1
    gp = 0
    sellday = 0
    buyday = 0
    lowest_stock_day = 0
    lowest_stock_day_price = a[0]
    for i in range(1, n):
      work = work + 1
      price_today = a[i]
      if price_today < lowest_stock_day_price:
        lowest_stock_day = i
        lowest_stock_day_price = price_today
      else:
        p = self._compute_profit(a, i, lowest_stock_day)
        if p > gp:
          gp = p
          buyday = lowest_stock_day
          sellday = i
    ans = [sellday, buyday, work]
    return ans
