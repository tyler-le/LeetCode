# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0
        
        def dfs(root):
            nonlocal range_sum
            if not root: return 0
            if low <= root.val <= high: range_sum += root.val
            if low < root.val: dfs(root.left)
            if high > root.val: dfs(root.right) 
            
            return range_sum
        
        return dfs(root)