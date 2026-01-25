# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height, is_balanced

        def dfs(node, curr_height):
            # base case
            if not node: return (0, True)

            # recursive step
            left_height, left_balanced = dfs(node.left, 1 + curr_height)
            right_height, right_balanced = dfs(node.right, 1 + curr_height)
            

            # return value
            is_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
            height = max(left_height, right_height) + 1
            return (height, is_balanced)

        _, is_balanced = dfs(root, 0)
        return is_balanced