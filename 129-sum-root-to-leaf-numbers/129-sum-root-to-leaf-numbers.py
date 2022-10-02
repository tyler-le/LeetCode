# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(node, curr_sum):
            
            if not node.right and not node.left:
                self.res+=curr_sum + node.val
                return
            
            curr_sum+=node.val
            
            if node.left: dfs(node.left, curr_sum*10)
            if node.right: dfs(node.right, curr_sum*10)
                
        dfs(root, 0)
        return self.res