#!/bin/python3

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import sys

def checkPrime(x, primelist):
    '''
        check if the number x is prime
        
        Parameters
        __________
        x: int
            value to check if prime   
        primelist:
            list of primes
       
       Returns
       _______
       boolean
           Whether number x is prime 
    '''
    for i in primelist:
        if x % i == 0:
            return False, primelist
    if i >= int(x**(0.5))+1:
        primelist.append(x)
        return True, primelist
    for i in range(i, int(x**(0.5))+1):
        if x % i == 0:
            return False, primelist
    primelist.append(x)
    return True, primelist

def solvePrime(n, primelist):
    '''
        gets the nth prime number
        
        Parameters
        __________
        n: int
            which prime number to return
        primelist: [int]
            list of primes in ascending order          
            
        Returns
        _______
        int
            nth prime number
    '''
    # retrieve if already calculated  
    lenlist = len(primelist)
    if lenlist >= n:
        return(primelist[n - 1], primelist)
            
    i = lenlist  # iterator
    val = primelist[-1] + 2
    while(True):
        isprime, primelist = checkPrime(val, primelist)
        if isprime:
            i += 1
        if i == n:
            break
        val += 2
    return val, primelist  

primelist = [2, 3]
if __name__ == '__main__':
  n = 10001
  ans, primelist = solvePrime(n, primelist)
  print(ans)
