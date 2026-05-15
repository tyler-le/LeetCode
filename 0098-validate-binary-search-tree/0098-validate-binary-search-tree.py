# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, mn, mx):
            if not node: return True
            if node.val <= mn or node.val >= mx: return False

            return is_valid(node.left, mn, node.val) and is_valid(node.right, node.val, mx)

    
        return is_valid(root, -math.inf, math.inf)