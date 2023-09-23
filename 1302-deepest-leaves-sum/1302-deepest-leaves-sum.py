# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # map depth : value                
        max_depth = 0
        res = 0
        
        def find_max_depth(depth, node):
            nonlocal max_depth
            if not node: return
            
            if not node.left and not node.right: 
                max_depth = max(max_depth, depth)
                return
            
            if node.left: find_max_depth(depth+1, node.left)
            if node.right: find_max_depth(depth+1, node.right)
        
        def dfs(depth, node):
            nonlocal max_depth
            nonlocal res
            
            if not node: 
                return
            
            if not node.left and not node.right and depth == max_depth:
                res+=node.val
                return
            
            if node.left: dfs(depth+1, node.left)
            if node.right: dfs(depth+1, node.right)
            
        find_max_depth(0, root)
        dfs(0, root)
        
        return res
        