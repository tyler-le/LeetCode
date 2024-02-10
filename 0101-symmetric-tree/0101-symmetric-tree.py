# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(p1, p2):
            if not p1 and not p2: return True
            if (p1 and not p2) or (not p1 and p2): return False
            if p1.val != p2.val: return False
            return rec(p1.left, p2.right) and rec(p1.right, p2.left)
        
        return rec(root, root)