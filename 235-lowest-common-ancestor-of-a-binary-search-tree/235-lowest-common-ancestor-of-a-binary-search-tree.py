# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        
        def dfs(curr):
            if curr.val > p.val and curr.val > q.val: 
                return dfs(curr.left)
            elif curr.val < p.val and curr.val < q.val: 
                return dfs(curr.right)
            else: 
                return curr
                
        return dfs(root)