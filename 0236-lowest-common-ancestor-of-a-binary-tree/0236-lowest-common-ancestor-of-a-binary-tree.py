# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # split

        # first to occur

        # if we find LCA on left AND right -> split case

        # if we find LCA on one side -> first to occur case

        def dfs(node):
            if not node: return None

            if node.val == p.val or node.val == q.val: 
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right: return node
            elif left and not right: return left
            else: return right

        return dfs(root)