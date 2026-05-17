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

            print(f"{node.val} has a max path of {curr + left + right}")
            if curr + left < curr:
                left = 0
            if curr + right < curr:
                right = 0


            res = max(res, curr + left + right)

            return curr + max(left, right)

        dfs(root)
        return res


