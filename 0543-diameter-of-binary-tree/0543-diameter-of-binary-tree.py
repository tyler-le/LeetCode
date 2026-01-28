# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # get_height() dfs for each node
        # diameter = left_height + right_height + 1
        # keep a global max

        res = 0
        def dfs(node):
            nonlocal res
            if not node: return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            diameter = left_height + right_height
            res = max(res, diameter)

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return res
