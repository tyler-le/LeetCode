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
        
        res, curr_path = [], []
        
        def dfs(node, curr_path, targetSum):
            if not node: return
            if node.left is None and node.right is None:
                if targetSum == node.val: res.append(curr_path[::] + [node.val])
                return
            
            curr_path.append(node.val)
            dfs(node.left, curr_path, targetSum - node.val)
            dfs(node.right, curr_path, targetSum - node.val)
            curr_path.pop()
            
        dfs(root, curr_path, targetSum)
        return res
            