# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        # return single branch height
        def dfs(node):
            nonlocal res
            if not node: return 0

            # diam is based off double branch height
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diam = left_height + right_height 
            res = max(res, diam)

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return res
        