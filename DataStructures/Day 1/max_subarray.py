#Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.

#if array = [1,2,3]
#subarrays will be: [1], [2], [3], [1,2], [2,3] ,[1,2,3]

#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #list for sum of subarrays
        sum_list = [1] * len(nums)

        #element 1 will be a part of sum subarray according to definition of subarrat
        sum_list[0] = nums[0]
        for i in range(1, len(nums)):
            #so sum list will have maximum between (sum of previous and courrent (ith) element)
            # and (element of given list)
            sum_list[i] = max(sum_list[i-1] + nums[i], nums[i])
            #in this wway we will get values of sum of contigous arrays if they are greate than our
            #list's values otherwise our list value will go in sum_list
        #as we have to return max sum so:
        return max(sum_list)


s = Solution()
a = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)