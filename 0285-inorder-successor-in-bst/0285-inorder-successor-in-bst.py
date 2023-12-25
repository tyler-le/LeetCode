# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        succ = None
        curr = root
        
        while curr:
            if curr.val <= p.val:
                curr = curr.right
            else:
                succ = curr
                curr = curr.left
                
        return succ
                