# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# this one is too slow, but with the reduce function
from functools import reduce

def failed_subfun(n):
    firstsum = sum(list(range(n+1))) ** 2
    secondsum = reduce((lambda x, y: x + y**2), list(range(1, n+1)))
    return firstsum - secondsum

# O(1)
def subfun(n):
    '''
      calculate the difference between the sum of squares and square of the sum of the first n natural numbers
      Parameters
      _________
      n: int 
        the biggest number in the range
      Returns
      _______
      the difference between the sum of squares and square of the sum of the first n natural numbers
    '''
    firstsum = int((n * (n+1) / 2) ** 2)
    secondsum = int(n * (n+1) * (2*n+1) / 6)
    return firstsum - secondsum
   
if __name__ == '__main__':
  n = 10
  print(subfun(n))
