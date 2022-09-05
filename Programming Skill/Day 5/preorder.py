#Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

#Input: root = [1,null,3,2,4,null,5,6]
#Output: [1,3,5,6,2,4]

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def preorder(root,arr):
            #check if root have the value 
            if root:
                #simply append it
                arr.append(root.val)
                #now we have to append its childeren 
                #so call function for its childers
                
                #so child refers to every child in node in children subtree
                for child in root.children:
                    preorder(child,arr)
            return arr
        return preorder(root,[])