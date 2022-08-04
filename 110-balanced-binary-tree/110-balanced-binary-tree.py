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
        
        def get_height(node):
            if not node: return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            return max(left_height, right_height) + 1
           
        if not root: return True
        left, right = get_height(root.left), get_height(root.right)
        if abs(left - right) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        