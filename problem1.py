# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# initial try, too slow for really large n
def find_multiples(n):
    mult = list(range(0,n,3))
    mult5 = (range(0,n,5))
    mult.extend(mult5)
    return sum(set(mult))

'''
    computes arithmetic sum for sequence with constant interval, eg 1, 3, 5, 7
    @param n - the upper bound
    @param x - interval between numbers in the sequence
'''
def arithmetic_sum(n, x):
    # divide the upper bound by the interval
    top = int(n / x)
    # bitwise shift operator to divide by 2, faster and more accurate without rounding errors
    seqsum =  (top * (top+1)) >> 1
    return int(x * seqsum)
    
if __name__ == '__main__':
  testn = 23
  print(arithmetic_sum(testn - 1, 3) + arithmetic_sum(testn - 1, 5) - arithmetic_sum(testn - 1, 15))
