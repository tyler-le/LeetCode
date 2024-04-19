# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            
            # if node.val == p.val or node.val == q.val -> LCA is node
            if node.val == p.val or node.val == q.val:
                return node
            
            # if p.val < node.val < q.val -> LCA is node
            if p.val < node.val < q.val:
                return node
            
            # if q.val < node.val < p.val -> LCA is node
            if q.val < node.val < p.val:
                return node
            
            # if node.val < (p.val and q.val) -> LCA is on the right
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)
            
            # if node.val > (p.val and q.val) -> LCA is on the left
            if node.val > p.val and node.val > q.val:
                return dfs(node.left)
            
        return dfs(root)
        
    