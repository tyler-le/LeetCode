# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(node, curr_depth):
            if not node: return None
            
            if curr_depth == depth-1:
                left = node.left
                right = node.right
                
                node.left = TreeNode(val)
                node.right = TreeNode(val)

                node.left.left = left
                node.right.right = right
            
            else:
                dfs(node.left, curr_depth+1)
                dfs(node.right, curr_depth+1)
            
            return node

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        return dfs(root, 1)