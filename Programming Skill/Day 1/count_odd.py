"""
        Problem:
            Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""

class Solution():
        
    """def countOdds(self, low, high):
        
        :type low: int
        :type high: int
        :rtype: int
        count = 0
        for i in range (low,high+1):
            if i % 2 != 0:
                count += 1
        return count


        Above is O(n) solution. That is taking too much time
        """

#this will take less time as it does not have any loops


    def countOdds(self, low, high) :
        #this will find odd numbers in between that range
        num_diff = (high - low) // 2
        
        #to check if high and low are odd or not
        if high % 2 != 0 or low % 2 != 0:
            num_diff = num_diff + 1
        
        return num_diff

                        

s = Solution()
odd = s.countOdds(3,7)
print(odd)
            
        