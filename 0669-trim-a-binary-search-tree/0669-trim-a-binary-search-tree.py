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
            
            # this node falls out of range. disregard node's left subtree
            elif node.val < low: return rec(node.right)
            
            # this node falls out of range. disregard node's right subtree
            elif node.val > high: return rec(node.left)
            
            # this node is within range, get the trimmed left and right subtrees recursively
            else: node.left, node.right = rec(node.left), rec(node.right)
                
            # return trimmed root
            return node
        
        return rec(root)