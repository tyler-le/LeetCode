# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # returns (height, isBalanced)
        def get_height(node):
            if not node: return (0, True)

            left_height, left_balanced = get_height(node.left)
            right_height, right_balanced = get_height(node.right)

            is_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced

            return (max(left_height, right_height) + 1, is_balanced)

        _, res = get_height(root)
        return res



        