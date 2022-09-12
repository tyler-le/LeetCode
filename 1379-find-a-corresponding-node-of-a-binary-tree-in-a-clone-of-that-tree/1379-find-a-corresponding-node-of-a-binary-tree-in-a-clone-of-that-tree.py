# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(orig, clone):
            if not orig: return
            if orig is target: self.ans = clone
            dfs(orig.left, clone.left)
            dfs(orig.right, clone.right)
           
            
        dfs(original, cloned)
        return self.ans