# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def rec(node):
            nonlocal res
            if not node: return 0
            left_sum = rec(node.left)
            right_sum = rec(node.right)
            if left_sum + right_sum == node.val:
                res+=1
            return left_sum + right_sum + node.val
        
        rec(root)
        return res