# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def rec(node):
            if not node.left and not node.right:
                if node.val == 0: return False
                else: return True
            
            else:
                if node.val == 2:
                    return rec(node.left) or rec(node.right)
                else:
                    return rec(node.left) and rec(node.right)
        
        return rec(root)