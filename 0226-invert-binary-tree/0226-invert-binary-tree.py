# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            # base case:
            if not node: 
                return None
            
            left, right = node.left, node.right
            node.left = right
            node.right = left
            
            dfs(node.left)
            dfs(node.right)
            
            return node
        
        return dfs(root)
        