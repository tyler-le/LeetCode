# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # two pass post order traversal
        
        res = 0
        
        def dfs(curr):
            nonlocal res
            if not curr: return [0,0]
            
            left_size, left_sum = dfs(curr.left)
            right_size, right_sum = dfs(curr.right)
            
            total_size = left_size + right_size + 1
            total_sum = left_sum + right_sum + curr.val
            
            average = total_sum // total_size
            if average == curr.val: res+=1
            
            return [total_size, total_sum]
            
        dfs(root)
        return res