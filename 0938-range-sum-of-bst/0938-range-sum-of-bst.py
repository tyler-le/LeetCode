# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node: return
            
            dfs(node.left)
            res+=(node.val if low <= node.val <= high else 0)
            dfs(node.right)
        
        dfs(root)
        
        return res