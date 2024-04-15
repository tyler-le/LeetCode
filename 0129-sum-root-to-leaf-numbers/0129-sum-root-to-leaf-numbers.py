# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            nonlocal res
            if not node:
                return 
            
            if not node.left and not node.right:
                res+=int("".join(path + [str(node.val)]))
                return
            
            if node.left:
                dfs(node.left, path + [str(node.val)])
            
            if node.right:
                dfs(node.right, path + [str(node.val)])
                    
        res = 0
        dfs(root, [])
        return res