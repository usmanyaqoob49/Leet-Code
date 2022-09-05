class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(1,n+1):
            #as we have 0s in last where we need to merge array 2
            if nums1[-i] == 0:
                #so we will start merging numbers from array 2 in array 1
                #in the end of array 1
                nums1[-i] = nums2[-i]
                     
        return nums1.sort()      