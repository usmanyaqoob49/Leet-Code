#Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. 
# If it is impossible to form any triangle of a non-zero area, return 0.

#Input: nums = [2,1,2]
#Output: 5

#Input: nums = [1,2,1]
#Output: 0 ---? becuse a + b > c and b + c >  a and c + a > b
#above is the must conditioni for the triangle


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
                        #i think starts from 0th index and fo to
                        #start      #stop  #step
        for i in range(len(nums) - 3, -1, -1):
            #necessary condition for forming a triangle
            #len of two sides must be greater than the third
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
        