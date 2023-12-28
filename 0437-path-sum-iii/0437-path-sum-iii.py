# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        res = 0
        prefix_sum = collections.defaultdict(int)
        
        def rec(node, curr_sum):
            nonlocal res
            if not node: return
            
            curr_sum+=node.val
            
            if curr_sum == targetSum: res+=1
            res+=prefix_sum[curr_sum - targetSum]
            
            prefix_sum[curr_sum]+=1
            
            rec(node.left, curr_sum)
            rec(node.right, curr_sum)
                
            prefix_sum[curr_sum]-=1
            
            
        rec(root, 0)
        return res