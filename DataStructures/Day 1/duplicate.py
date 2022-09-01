#Given an integer array nums, 
# return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #I can make a list of distinct unique elements using set() 
        # and we can compare it with list and if legth is same 
        # it means no repition other wise there is repeated elements

        unique_list = set(nums)
        if len(unique_list) == len(nums):
            #means no repetition so return false
            return False
        else:
            return True    