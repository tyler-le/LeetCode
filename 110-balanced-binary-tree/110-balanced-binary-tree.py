# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            if not root:
                return 0
            
            left_height = get_height(root.left)
            right_height = get_height(root.right)
            
            return max(left_height, right_height) + 1
        
        if not root:
            return True
        if abs(get_height(root.left) - get_height(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)