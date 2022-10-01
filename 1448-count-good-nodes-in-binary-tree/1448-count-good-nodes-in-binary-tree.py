# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of the max of the path
        self.res = 0
        def dfs(node, path):
            if not node: return
            if not path or node.val >= max(path): 
                self.res+=1
            
            path.append(node.val)
        
            if node.left: dfs(node.left, path)
            if node.right: dfs(node.right, path)
                
            path.pop()
        
        
        dfs(root, [])
        return self.res