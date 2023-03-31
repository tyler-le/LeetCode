# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def helper(p1, q1):
            if not p1 and not q1: return True
            if (not p1 and q1) or (p1 and not q1) or (p1.val != q1.val):
                return False
            return helper(p1.left, q1.left) and helper(p1.right, q1.right)
                    
        return helper(p, q)
        
        
        