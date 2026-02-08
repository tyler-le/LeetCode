# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # returns the height of a node
        def dfs(node):
            if not node: return (0, True)
            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)

            height = 1 + max(left_height, right_height)
            is_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
            
            return (height, is_balanced)
        
        return dfs(root)[1]