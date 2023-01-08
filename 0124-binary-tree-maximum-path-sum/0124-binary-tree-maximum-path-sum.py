# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root: return 0
            left, right = max(helper(root.left), 0), max(helper(root.right), 0)
            local_max = left + right + root.val 
            self.global_max = max(self.global_max, local_max)
            return max(left, right) + root.val
        
        # max path sum of left + root.val + max path sum of right
        self.global_max = -float('inf')
        helper(root)
        return self.global_max
        
        
            
            
        