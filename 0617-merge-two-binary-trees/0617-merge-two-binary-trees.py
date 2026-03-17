# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(p1, p2):
            if not p1 and not p2: return None
            if p1 and not p2: return p1
            if not p1 and p2: return p2

            node = TreeNode(p1.val + p2.val)
            
            left = dfs(p1.left, p2.left)
            right = dfs(p1.right, p2.right)

            node.left = left
            node.right = right

            return node


        return dfs(root1, root2)