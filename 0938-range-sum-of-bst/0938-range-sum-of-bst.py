# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        res = 0
        
        def dfs(node):
            nonlocal arr
            if not node: return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        for num in arr:
            res+=(num if low <= num <= high else 0)
        return res