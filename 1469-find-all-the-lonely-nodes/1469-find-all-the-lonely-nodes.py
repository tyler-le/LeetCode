# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def dfs(node):
            nonlocal res
            if not node: return
            
            if (not node.left and node.right):
                res.append(node.right.val)
            elif (node.left and not node.right):
                res.append(node.left.val)
                
            
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return res