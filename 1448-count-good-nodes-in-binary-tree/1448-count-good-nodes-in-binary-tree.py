# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def rec(node, maxi):
            nonlocal res
            if not node: return
            if node.val >= maxi: res+=1
            rec(node.left, max(maxi, node.val))
            rec(node.right, max(maxi, node.val))
            
        
        rec(root, root.val)
        return res