# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def dfs(root):
            if root is None:
                return 0
            return max( dfs(root.left), dfs(root.right))  + 1
            
        return dfs(root)
        