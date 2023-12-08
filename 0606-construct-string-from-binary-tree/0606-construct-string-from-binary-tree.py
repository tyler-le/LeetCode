# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
                
        def preorder(node):
            
            if not node: return ""
                
            s = str(node.val)
            
            if node.left: s += "(" + preorder(node.left) + ")"
            elif node.right and not node.left: s+="()"
            if node.right: s+="(" + preorder(node.right) + ")"
                
            return s
        
        return preorder(root)
