# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = 0
        
        def rec(node):
            nonlocal res
            if not node: return (0, 0)
            left_sum, left_size = 0, 0
            right_sum, right_size = 0, 0
            
            if node.left: left_sum, left_size = rec(node.left)
            if node.right: right_sum, right_size = rec(node.right)
            
            sumi = node.val + left_sum + right_sum
            size = 1 + left_size + right_size
            res = max(res, sumi/size)
            
            return (sumi, size)
        
        rec(root)
        return res