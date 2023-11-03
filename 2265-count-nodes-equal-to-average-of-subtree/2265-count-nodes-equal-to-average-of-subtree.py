# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            if not root: return [0,0]
            
            left_size, left_sum = dfs(root.left)
            right_size, right_sum = dfs(root.right)
            
            curr_size = left_size + right_size + 1
            curr_sum = left_sum + right_sum + root.val
            curr_avg = curr_sum // curr_size
            
            res += (1 if curr_avg == root.val else 0)
            
            return [curr_size, curr_sum]
        
        dfs(root)
        return res
            
        