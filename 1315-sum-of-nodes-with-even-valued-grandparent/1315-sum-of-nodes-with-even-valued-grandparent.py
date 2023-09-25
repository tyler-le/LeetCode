# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # traverse tree while keeping track of parent and grandparent
        res = 0
        
        def dfs(node, parent, grandparent):
            nonlocal res
            if not node: return
            
            dfs(node.left, node, parent)
            if grandparent and grandparent.val % 2 == 0: res+=node.val
            dfs(node.right, node, parent)
        
        dfs(root, None, None)
        return res
            