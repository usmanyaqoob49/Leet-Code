#Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
#Input: n = 234
#Output: 15 
#Explanation: 
#Product of digits = 2 * 3 * 4 = 24 
#Sum of digits = 2 + 3 + 4 = 9 
#Result = 24 - 9 = 15
class Solution():
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        sum_num = 0
        result = 0
        n = str(n)
        for char in n:
            num = int(char)
            sum_num += num
            prod = prod * num
        result = prod - sum_num
        return result