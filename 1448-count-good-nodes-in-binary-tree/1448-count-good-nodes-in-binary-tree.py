# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        def dfs(root):
            
            if not root:
                return 0
            if visited and root.val >= max(visited):
                res = 1 
            else:
                res = 0
                
            visited.append(root.val)
            res += dfs(root.left)
            res += dfs(root.right)
            visited.pop()
            return res
            
            
        visited = []
        return dfs(root)+1
        