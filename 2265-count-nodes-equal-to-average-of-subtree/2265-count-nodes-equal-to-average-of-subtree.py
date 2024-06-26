# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        
        def rec(node):
            nonlocal res
            if not node: return (0, 0)
            
            left_sum, left_size = rec(node.left)
            right_sum, right_size = rec(node.right)
            
            curr_sum = left_sum + right_sum + node.val
            curr_total = 1 + left_size + right_size
            average = curr_sum // curr_total
            
            if average == node.val: 
                res+=1
            
            return (curr_sum, curr_total)
        
        rec(root)
        return res