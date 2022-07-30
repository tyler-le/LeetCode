# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        range_sum = [0]
        def dfs(root, range_sum): 
            if not root: return 
            if low <= root.val <= high: 
                range_sum[0] = range_sum[0] + root.val
                print(root.val)
            dfs(root.left, range_sum)
            dfs(root.right, range_sum)
            return range_sum[0]
        
        return dfs(root, range_sum)
        