# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        acc = 0
        
        def dfs(root):
            
            nonlocal acc
            if not root: return
            
            if root.right: dfs(root.right)
            root.val += acc
            acc = root.val
            if root.left: dfs(root.left)
            
            return
        
        dfs(root)
        return root
        
        