# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root, None)
        
        def dfs(node, d):
            if not node: return
            left, right = node.left, node.right
            if d == depth - 1:
                node.left = TreeNode(val, left, None)
                node.right = TreeNode(val, None, right)
            
            dfs(left, d+1)
            dfs(right, d+1)
            
            
        dfs(root, 1)
        return root
            