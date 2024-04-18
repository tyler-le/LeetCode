# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # find the difference of height of left and right subtrees.
        # repeat recursively on left and rights
        
        
        def dfs(node):
            nonlocal res
            if not node: return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left - right) > 1:
                res = False
            
            return 1 + max(left, right)
        
        res = True
        dfs(root)
        return res
        