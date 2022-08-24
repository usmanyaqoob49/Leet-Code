import re


class Solution(object):


    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sum = 0
        maxi = max(salary)
        mini = min(salary)
        for i in salary:
            sum += i
        return (sum - maxi - mini )/(len(salary)-2)
    

s = Solution()
a = s.average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000])     
print(a)