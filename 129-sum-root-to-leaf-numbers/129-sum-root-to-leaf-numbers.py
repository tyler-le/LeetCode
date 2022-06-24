# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum_numbers_helper(root, 0)
        
    def sum_numbers_helper(self, root, path_sum):
        if not root:
            return 0
        
        path_sum = (10*path_sum)+root.val
        
        is_leaf = root.right is None and root.left is None
        if is_leaf:
            return path_sum
        
        return self.sum_numbers_helper(root.left, path_sum) + self.sum_numbers_helper(root.right, path_sum)
        