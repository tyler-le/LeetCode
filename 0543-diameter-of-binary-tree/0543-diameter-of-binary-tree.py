# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = max height from left subtree + max height from right subtree
        res = 0
        
        def get_height(node):
            nonlocal res
            if not node: return 0
            
            left = get_height(node.left)
            right = get_height(node.right)
            res = max(res, left + right)
            return max(left, right) + 1
        
        get_height(root)
        return res