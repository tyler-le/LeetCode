# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def rec(node):
            if not node: return None
            elif node.val < low: return rec(node.right)
            elif node.val > high: return rec(node.left)
            else:
                node.left = rec(node.left)
                node.right = rec(node.right)
            
            
            
            return node
        
        return rec(root)