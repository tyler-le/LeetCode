# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q: return True
            elif p and not q or not p and q: return False
        
            if p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
        
        if not root and not subRoot: return True
        if not root and subRoot: return False
        if root and not subRoot: return True
        
        if isSameTree(root, subRoot): return True
        else: return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    