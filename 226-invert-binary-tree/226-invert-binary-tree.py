# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        stack.append(root)
        
        while len(stack) != 0:
            curr = stack.pop()
            if curr is not None:
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
                stack.append(curr.left)
                stack.append(curr.right)
                
        return root
            
        