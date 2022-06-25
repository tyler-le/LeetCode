# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max_sum = -math.inf
        
        def max_path_sum_helper(root):
            if not root:
                return 0
            
            max_left_sum = max(max_path_sum_helper(root.left),0)
            max_right_sum = max(max_path_sum_helper(root.right),0)
            
            local_max_sum = max_left_sum + max_right_sum + root.val
            
            self.global_max_sum = max(local_max_sum, self.global_max_sum)
            
            return max(max_left_sum, max_right_sum) + root.val
        
        
        max_path_sum_helper(root)
        return self.global_max_sum