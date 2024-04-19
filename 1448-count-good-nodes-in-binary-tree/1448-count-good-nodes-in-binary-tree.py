# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node, mx_in_path):
            nonlocal res
            
            if not node: return
            
            if node.val >= mx_in_path: res+=1
            
            dfs(node.left, max(node.val, mx_in_path))
            dfs(node.right, max(node.val, mx_in_path))
        
        dfs(root, root.val)
        return res