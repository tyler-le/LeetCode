# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        
        # find longest depth rooted at node
        def get_height(node):
            nonlocal max_diam
            
            if not node:
                return 0
            
            left = get_height(node.left)
            right = get_height(node.right)
            
            max_diam = max(max_diam, left + right)
            
            return 1 + max(left, right)
            
        get_height(root)
        return max_diam