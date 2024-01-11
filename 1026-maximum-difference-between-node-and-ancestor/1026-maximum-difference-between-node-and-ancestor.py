# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr_min, curr_max):
            if not node: return curr_max - curr_min

            left = dfs(node.left, min(curr_min, node.val), max(curr_max, node.val))
            right = dfs(node.right, min(curr_min, node.val), max(curr_max, node.val))
            
            return max(left, right)
            
        return dfs(root, root.val, root.val)