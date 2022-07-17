# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q) or (p.val != q.val):
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if not root:
            return False
        
        if root and subRoot and root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)