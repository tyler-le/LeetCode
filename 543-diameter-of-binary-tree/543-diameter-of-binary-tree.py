# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        
        def dfs(root):
            if not root:
                return 0
            
            left_height, right_height = dfs(root.left), dfs(root.right)
            curr_diameter = left_height + right_height
            self.max_diameter = max(self.max_diameter, curr_diameter)
            
            return max(left_height, right_height) + 1
            
        dfs(root)
        return self.max_diameter