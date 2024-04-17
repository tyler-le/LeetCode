# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = "~"
        
        def dfs(node, curr):
            nonlocal res
            
            curr += chr(node.val + ord('a'))
            
            if not node.left and not node.right:
                res = min(res, curr[::-1])
                return

            if node.left: dfs(node.left, curr)
            if node.right: dfs(node.right, curr)
        
        dfs(root, "")
        return res
            