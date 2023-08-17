# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(nodeL, nodeR, height):
            
            if not nodeL or not nodeR:
                return
                        
            if height % 2 == 0:
                nodeL.val, nodeR.val = nodeR.val, nodeL.val
            
            dfs(nodeL.left, nodeR.right, height+1)
            dfs(nodeL.right, nodeR.left, height+1)
                                
        dfs(root.left, root.right, 0)
        return root
