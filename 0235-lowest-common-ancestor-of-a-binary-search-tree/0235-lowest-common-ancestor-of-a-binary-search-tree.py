# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def rec(node):
            
            if (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
                return node
            elif p.val < node.val and q.val < node.val:
                return rec(node.left)
            elif p.val > node.val and q.val > node.val:
                return rec(node.right)
        
        return rec(root)
                