# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # return the LCA
        def dfs(node):

            # base case
            if not node: return None

            # if split, return node
            if p and q and p.val < node.val < q.val: return node
            if p and q and p.val > node.val > q.val: return node
            
            # encounter p or q
            if node.val == p.val: return node
            if node.val == q.val: return node

            # recurse
            left, right = False, False
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
        
        return dfs(root)
