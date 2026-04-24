# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        FALSE, TRUE, OR, AND = 0, 1, 2, 3

        def dfs(node):

            if not node.left and not node.right:
                return node.val
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == AND:
                return left and right
            else:
                return left or right
        
        return dfs(root) == TRUE