# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        left, right = 0, 1
        res = 0
        
        def dfs(node, direction, steps):
            nonlocal res
            
            if not node: return
            res = max(res, steps)
            
            if direction == left:
                dfs(node.left, left, 1)
                dfs(node.right, right, steps+1)
            else:
                dfs(node.left, left, steps+1)
                dfs(node.right, right, 1)
            
        dfs(root, left, 0)
        dfs(root, right, 0)
        
        return res
            