#A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

#Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. 
# Otherwise, return false.

#Input: arr = [3,5,1]
#Output: true
#Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, 
# between each consecutive elements.


class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #checking the correct length
        if len(arr) < 2:
            return

        #sorting to check the condition        
        arr.sort()

        #finding the differnece so that we can compare
        dif = arr[1] - arr[0]
        for i in range (0,len(arr)-1):
            
            if arr[i+1] - arr[i] != dif :
                return False
        
        return True
        