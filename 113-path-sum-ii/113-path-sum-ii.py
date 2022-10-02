# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        res = []
        def dfs(node, curr_path):
            if not node: return
            
            if not node.left and not node.right:
                if sum(curr_path + [node.val]) == targetSum: 
                    res.append(curr_path[::] + [node.val])
                return
            
            if node.left: dfs(node.left, curr_path + [node.val])
            if node.right: dfs(node.right, curr_path + [node.val])
        
        dfs(root, [])
        return res