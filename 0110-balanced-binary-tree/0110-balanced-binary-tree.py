# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node: return (True, 0)
            left_balanced, left_height = get_height(node.left)
            right_balanced, right_height = get_height(node.right)

            height = 1 + max(left_height, right_height)

            if abs(left_height - right_height) > 1:
                return (False, height)
            else:
                return (left_balanced and right_balanced, height)
        
        return get_height(root)[0]
