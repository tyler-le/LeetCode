# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        res = -float("inf")
        def dfs(node, ancestors):
            nonlocal res
            
            if not node: return 
            for a in ancestors:
                res = max(res, abs(node.val - a))
                
            dfs(node.left, ancestors + [node.val])
            dfs(node.right, ancestors + [node.val])
        
        dfs(root, [])
        return res
            
            