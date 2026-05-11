# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        LEFT, RIGHT = 0, 1
        res = 0
        
        @cache
        def dfs(node, prev_dir, dist):
            nonlocal res
            longest = 0
            if not node: return dist - 1

            # continue with zig-zag
            if prev_dir == LEFT:
                longest = max(longest, dfs(node.right, RIGHT, 1 + dist))
            else:
                longest = max(longest, dfs(node.left, LEFT, 1 + dist))
            
            # do not continue (start new)
            if prev_dir == LEFT:
                longest = max(longest, dfs(node.left, LEFT, 1))
            else:
                longest = max(longest, dfs(node.right, RIGHT, 1))
            
            res = max(res, longest)
            return longest
        
        return max(dfs(root, LEFT, 0), dfs(root, RIGHT, 0))
