############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################
############################################################
# All imports
###########################################################
from Util import *

class Solution:
  def __init__(self,n:'int',a:'list of size 2'):
    self._n = n
    #a[0] = How many friends are there in n
    #a[1] = num_steps
    self._list = a
    ##YOU CAN HAVE ANY NUMBER OF DATA STRUCTURES HERE

    # create util instance for sqrt
    self._u = Util()
    # create the list of prime numbers up to n
    self._primes_table = self._sieve_of_eratosthenes(self._n)

  ##Required function to implement
  def friends(self):
    ## NOTHING CAN BE CHANGED HERE
    self._alg()
 
  ##Implement your code BELOW
  ##You can have any number of private variables and functions

  def _alg(self):
    calc1 = []
    calc2 = []
    output = []
    for i in range(self._n + 1): # 0, 1, 2, 3, ..., n
      calc1.append(self._fact_sum(i))
      self._list[1] += 1 # work done
    for i in range(self._n + 1):
      try:
        calc2.append(calc1[calc1[i]])
      except IndexError:
        calc2.append(self._fact_sum(calc1[i]))
      if i == calc2[i] and i < calc1[i]:
        output.append((i, calc1[i]))
      self._list[1] += 1 # work done
    self._list[0] = len(output)

  # list of prime numbers
  def _sieve_of_eratosthenes(self, n: 'int') -> 'list':
    primes = [True] * (n + 1)
    primes[0] = False # 0 is not a prime number
    primes[1] = False # 0 is not a prime number
    sqrtn = self._u.sqrt_upper_bound(n)
    for i in range(2, sqrtn):
      if primes[i] == True:
        # if i = 10
        # i = 10 10 10 10 10
        # k = 10 11 12 13
        # j = 100 110 120 130
        k = i # do not need to start from 1
        j = i
        while True:
          j = i * k
          if j >= n + 1:
            break
          primes[j] = False
          k = k + 1
          self._list[1] += 1 # work done
    return [i for i in range(n + 1) if primes[i] == True]

  # sum of factors
  def _sum_factors(self, factors: 'list') -> 'int':
    sum_output = 1
    num_factors = len(factors)
    for i in range(num_factors):
      temp = 0
      for j in range(factors[i][1] + 1):
        temp += factors[i][0] ** j
        self._list[1] += 1 # work done
      sum_output *= temp
    if factors[0][0] in (0, 1):
      sum_output -= 1
    return sum_output

  # factorization and sum
  def _fact_sum(self, n: 'int') -> 'list':
    factors = [] # 12 -> [[2, 2], [3, 1]]
    temp = n
    sqrtn = self._u.sqrt_upper_bound(n)
    for i in self._primes_table:
      if i > sqrtn:
        break
      else:
        if temp % i == 0:
          power = 0
          while temp % i == 0:
            power += 1
            temp //= i
            self._list[1] += 1 # work done
          factors.append([i, power])
    if temp != 1:
      factors.append([temp, 1])
    if factors == []:
      factors.append([n, 1])
    total_sum = self._sum_factors(factors)
    return total_sum - n