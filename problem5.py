#!/bin/python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def findfactors(n):
    '''
        finds all factors of number n
        
        Parameters
        ----------
        n : int
            number n for which we are finding the factors
        
        Returns 
        _______
        list of ints
            dictionary of the factors of n
    '''
    factors = {}
    orign = n
    x = 2
    while x < int(orign**0.5 + 1):
        if n % x == 0:
            if x in factors:
                factors[x] = factors[x] + 1
            else:
                factors[x] = 1
            n = n/x 
            if n == 1:
                break
        else:
            x += 1
    if n == orign:
        factors[orign] = 1 
    return factors    
    
    
def scd(listn):
    '''
        finds the smallest number that can be divided by each number in listn
        
        Parameters
        __________
        listn : list of ints
            list of numbers for which we are finding the smallest common divisible
        
        Returns:
        int
            the smallest number that can be divided by each number in listn
            
    '''
    factordict = {}
    for n in listn:
        nfactors = findfactors(n)
        for fact in nfactors:
            if fact in factordict:
                factordict[fact] = max(factordict[fact], nfactors[fact])
            else:
                factordict[fact] = nfactors[fact]
    product = 1
    for fact in factordict:
        product *= fact ** factordict[fact]
    return product
    
    if __name__ == '__main__':
      # example
      n = 20
      print(scd(list(range(1,n+1))))
