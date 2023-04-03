# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if not node: return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)
            
        nodes = []        
        preorder(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1] 
            