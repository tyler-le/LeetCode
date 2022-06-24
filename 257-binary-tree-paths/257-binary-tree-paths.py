# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(root, res, curr_path):
            if not root:
                return
            
            is_leaf = root.left is None and root.right is None
                
            if is_leaf:
                curr_path += str(root.val)
                res.append(curr_path)
            else:
                curr_path = curr_path + str(root.val) + "->" 
                
            dfs(root.left, res, curr_path)
            dfs(root.right, res, curr_path)
                
  
        res = []
        dfs(root, res, "")
        return res
        