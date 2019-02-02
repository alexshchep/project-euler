# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers (that is less than N).

def divisibleList(y, divisorlist):
    '''
        Iterates through a divisorlist to divide y by.
        If y is divisible by two numbers in divisorlist, returns True, else returns False
        @param y - the dividend
        @param dividelist - list of divisors
    '''
    val = next((x for x in divisorlist if y % x == 0 and (y/x) in divisorlist), 0)
    if val != 0:
        return True
    else:
        return False

def findLargestPalindrome(n, palindromelist, digitlist):
    '''
        Find largest palindrome 6-digit that is a product of two 3 digit numbers 
        but smaller than n.
        Figure out palindrome first then try to divide
        @param n - palindrome has to be smaller than this number
        @param palindromelist - sorted from hi to lo list of acceptable palindromes
        @param digitlist - values that palindrome needs to be divisible by 
    '''
    # keep only numbers that are smaller than n
    templist = [x for x in palindromelist if x < n]
    # iterate through templist to check if divisible by 3 digit number
    largest = next((x for x in templist if divisibleList(x, digitlist)), 0) # returns 0 if no match is found)
    return largest

if __name__ == '__main__':   
  palindromelist = [int(str(x) + str(x)[::-1]) for x in range(999, 99, -1)]    
  threedigitlist = list(range(100,1000))
  print(findLargestPalindrome(1000000, palindromelist, threedigitlist))
  
