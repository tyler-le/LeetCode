# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node: return (0, 0)
            
            left, right = dfs(node.left), dfs(node.right)
            
            # rob the current node
            rob = node.val + left[1] + right[1]
            
            # do not rob the current node
            no_rob = max(left) + max(right)
            
            return (rob, no_rob)
        
        return max(dfs(root))