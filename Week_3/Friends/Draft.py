import math

# list of prime numbers
def _sieve_of_eratosthenes(n: 'int') -> 'list':
    a = [0, 0] # a[0] is number of prime, a[1] is number of steps
    primes = [True] * (n + 1)
    primes[0] = False # 0 is not a prime number
    primes[1] = False # 0 is not a prime number
    sqrtn = math.ceil(math.sqrt(n)) # self._u.sqrt_upper_bound(self._n)
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
                a[1] += 1 # work done
                primes[j] = False
                k = k + 1
    return [i for i in range(n + 1) if primes[i] == True]

primes_table = _sieve_of_eratosthenes(n) # sqrt(n) is enough

# sum of factors
def sum_factors(factors: 'list') -> 'int':
    sum_output = 1
    num_factors = len(factors)
    for i in range(num_factors):
        temp = 0
        for j in range(factors[i][1] + 1):
            temp += factors[i][0] ** j
        sum_output *= temp
    if factors[0][0] in (0, 1):
        sum_output -= 1
    return sum_output

# factorization and sum
def fact_sum(n: 'int') -> 'list':
    factors = [] # 12 -> [[2, 2], [3, 1]]
    temp = n
    sqrtn = math.ceil(math.sqrt(n)) # self._u.sqrt_upper_bound(self._n)
    for i in primes_table:
        if i > sqrtn:
            break
        else:
            if temp % i == 0:
                power = 0
                while temp % i == 0:
                    power += 1
                    temp //= i
                factors.append([i, power])
    if temp != 1:
        factors.append([temp, 1])
    if factors == []:
        factors.append([n, 1])
    total_sum = sum_factors(factors)
    return total_sum - n

# output amicable numbers
def amicable(n):
    calc1 = []
    calc2 = []
    output = []
    for i in range(n + 1): # 0, 1, 2, 3, ..., n
        calc1.append(fact_sum(i))
    for i in range(n + 1):
        try:
            calc2.append(calc1[calc1[i]])
        except IndexError:
            calc2.append(fact_sum(calc1[i]))
        if i == calc2[i] and i < calc1[i]:
            output.append((i, calc1[i]))
    return output