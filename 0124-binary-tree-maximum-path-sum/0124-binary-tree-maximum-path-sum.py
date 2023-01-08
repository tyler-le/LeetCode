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
            
            # recursively find left and right
            # if they are negative then we choose not to pick them
            left, right = max(helper(root.left), 0), max(helper(root.right), 0)
            
            # update maxes
            local_max = left + right + root.val 
            self.global_max = max(self.global_max, local_max)
            
            # can only take left branch OR right branch, 
            # but not both in next recursive call
            # "A node can only appear in the sequence at most once"
            return max(left, right) + root.val
        
        self.global_max = -float('inf')
        helper(root)
        return self.global_max
        
        
            
            
        