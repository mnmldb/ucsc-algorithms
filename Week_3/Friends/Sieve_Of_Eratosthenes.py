import math

def _sieve_of_eratosthenes(n: 'int') -> 'list':
    #O(n) space
    #O(n) time
    l = []
    a = [0, 0] # a[0] is number of prime, a[1] is number of steps
    for i in range(n + 1):
        a[1] += 1 # work done
        l.append(True) # [True, True, True, ... , True]
    l[0] = False # 0 is not a prime number
    l[1] = False # 1 is not a prime number
    sqrtn = int(math.sqrt(n))
    for i in range(2, sqrtn):
        if l[i] == True:
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
                l[j] = False
                k = k + 1
    # now get number of primes
    for i in range(n + 1):
        a[1] += 1 # work done
        if l[i] == True:
            a[0] += 1
    return a