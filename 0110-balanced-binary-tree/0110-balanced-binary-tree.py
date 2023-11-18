# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def rec(root):
            if not root: return (0, True)
            
            left_height, left_balanced = rec(root.left)
            right_height, right_balanced = rec(root.right)
            
            is_balanced = abs(left_height - right_height) <= 1
            
            return (1 + max(left_height, right_height), is_balanced and left_balanced and right_balanced)
        
        
        return rec(root)[1]