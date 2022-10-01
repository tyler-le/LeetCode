# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        mem = []
        def preorder(node):
            if not node: return
            mem.append(node)
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        for i in range(len(mem) - 1):
            mem[i].right = mem[i+1]
            mem[i].left = None
        return root