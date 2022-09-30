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
        
        def backtrack(curr_node, targetSum, path):
            if not curr_node: return
            
            is_leaf = curr_node.left is None and curr_node.right is None
            
            if is_leaf and curr_node.val == targetSum:
                res.append(path[::] + [curr_node.val])
                return
            
            path.append(curr_node.val)
            backtrack(curr_node.left, targetSum - curr_node.val, path)
            backtrack(curr_node.right, targetSum - curr_node.val, path)
            path.pop()
            
        backtrack(root, targetSum, [])
        return res
        