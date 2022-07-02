# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # dfs, find height of left subtree and find height of right subtree
        self.is_balanced = True
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if abs(left - right) > 1:
                self.is_balanced = False
            
            return 1 + max(left, right) 
        
        
        dfs(root)
        return self.is_balanced