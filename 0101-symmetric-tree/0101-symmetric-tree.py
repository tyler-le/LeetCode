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
            
            elif (not p1 and p2) or (p1 and not p2): return False
            
            elif p1.val != p2.val: return False
            
            else:
                first = rec(p1.left, p2.right)
                second = rec(p1.right, p2.left)
            
            return first and second
        
        return rec(root, root)