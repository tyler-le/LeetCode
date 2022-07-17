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
        
        
        def dfs(root, max_val):
            if not root:
                return 0
            
            res = 1 if (root.val >= max_val) else 0
                
            #visited.append(root.val)
            max_val = max(max_val, root.val)
            res += dfs(root.left, max_val)
            res += dfs(root.right, max_val)
            return res
             
        return dfs(root, root.val)
        