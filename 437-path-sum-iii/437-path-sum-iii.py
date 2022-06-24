# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def path_sum_helper(root, targetSum, curr_path):
            
            if root is None:
                return 0
            
            curr_path.append(root.val)
                
            # check sums of all subpaths in curr_path here
            count, curr_sum = 0, 0
            for i in range(len(curr_path)-1, -1, -1): # reverse iteration
                curr_sum+=curr_path[i]
                if curr_sum == targetSum:
                    count += 1
                
            count += path_sum_helper(root.left, targetSum, curr_path)
            count += path_sum_helper(root.right, targetSum, curr_path)
            
            del curr_path[-1]
            
            return count
        
        return path_sum_helper(root, targetSum, [])
        