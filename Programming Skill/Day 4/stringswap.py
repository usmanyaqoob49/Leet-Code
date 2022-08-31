#You are given two strings s1 and s2 of equal length. 
# A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.


#Input: s1 = "bank", s2 = "kanb"
#Output: true
#Explanation: For example, swap the first character with the last character of s2 to make "bank".


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        #firstly we will check if we can get both string equals after sorting both
        if sorted(s1) != sorted(s2):
            return False
        
        
        count = 0
        for i in range (len(s1)):
            if s1[i] != s2[i]:
                count += 1
                
        #if we have differnce of two characters it mean that is ok we can swap and strings will
        #be sae
            
        if count == 2 or count == 0:
            return True
        else:
            return False
        