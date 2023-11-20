# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        
        def dfs(node, path_max):
            nonlocal res
            if node.val >= path_max: res+=1
            path_max = max(node.val, path_max)
            
            if node.left: dfs(node.left, path_max)
            if node.right: dfs(node.right, path_max)
                
        dfs(root, root.val)
        return res