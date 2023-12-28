# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # inorder traversal
        
        l1, l2 = [], []
        
        def inorder(node, arr):
            if not node: 
                return
            if not node.left and not node.right: 
                arr.append(node.val)
                
            inorder(node.left, arr)
            inorder(node.right, arr)
        
        inorder(root1, l1)
        inorder(root2, l2)

        return l1 == l2