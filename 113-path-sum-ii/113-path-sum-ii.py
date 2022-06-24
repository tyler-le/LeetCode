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
        self.path_sum_helper(root, targetSum, [], res)
        return res
        
    def path_sum_helper(self,root, targetSum, curr_path, res):
        if not root:
            return
        
        curr_path.append(root.val)
        is_leaf = root.left is None and root.right is None
        
        if is_leaf and root.val==targetSum:
            res.append(list(curr_path))
        
        else:          
            self.path_sum_helper(root.left, targetSum-root.val, curr_path,res)
            self.path_sum_helper(root.right, targetSum-root.val,curr_path,res)
        
        del curr_path[-1]

        