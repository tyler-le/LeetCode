# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = -math.inf
        # return max(left, right)
        
        def dfs(node):
            nonlocal res
            if not node: return 0
            
            curr = node.val
            left = dfs(node.left)
            right = dfs(node.right)

            # if adding left makes it bigger
            if curr + left < curr: left = 0

            # if adding right makes it bigger
            if curr + right < curr: right = 0

            res = max(res, curr + left + right)

            return curr + max(left, right)

        dfs(root)
        return res


