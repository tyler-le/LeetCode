# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return
            
            left, right = None, None
            
            if node.left: left = helper(node.left)
            if node.right: right = helper(node.right)
                
            if node.left and node.right:
                node.left = right
                node.right = left
            elif not node.left and node.right:
                node.left = right
                node.right = None
            else:
                node.right = left
                node.left = None
            
            return node
                
        return helper(root)