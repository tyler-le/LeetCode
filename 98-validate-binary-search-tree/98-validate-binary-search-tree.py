# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inord = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inord.append(root.val)
            inorder(root.right)
            
        # get inorder traversal
        inorder(root)
        
        for i in range(len(inord)-1):
            if inord[i] >= inord[i+1]:
                return False
        
        return True