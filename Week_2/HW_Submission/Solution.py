############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################
class Solution:
  def __init__(self):
    pass

  #THIS IS LEETCODE
  def  countAndSay(self,n:'int')->'string':
    ## NOTHING CAN BE CHANGED HERE
    return self._alg_integer(n)

  def  countAndSayString(self,n:'string')->'string':
    #Nothing can be changed here
    return self._alg_string(n) 

  ### YOU CAN HAVE ANY NUMBER OF FUNCTIONS AND CLASSES BELOW

  def _alg_string(self,n:'string')->'string':
    l = list(n)
    nums = len(l)
    
    prev = l[0] # initial number
    cnt = 1 # initial iteration
    output = ''
    
    for i in range(1,nums):
        if l[i] != prev:
            output += str(cnt)
            output += prev
            cnt = 1 # reset cnt
            prev = l[i]
        else: # l[i] == prev
            cnt += 1
    
    output += str(cnt)
    output += prev
    
    return output
  
  def _alg_integer(self,n:'int')->'string':
    output = '1'
    while n > 1:
        output = self._alg_string(output)
        n -= 1
    return output