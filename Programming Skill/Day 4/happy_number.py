#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.


#Input: n = 19
#Output: true
#Explanation:
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache = set()
        #recursive function to pass n to find square of every digit and checking conditions again
        def recursive_call(n):
            #if we got n means we found that number is happy
            if n == 1:
                return True
            
            #numbers other than 1 will be in cache
            if n in cache:
                return False
            
            cache.add(n)
            n = str(n)
            sum = 0
            square = 0
            
            for ch in n:
                ch = int(ch)
                square = ch ** 2
                sum += square
            return recursive_call(sum)
        return recursive_call(n)
                
                    