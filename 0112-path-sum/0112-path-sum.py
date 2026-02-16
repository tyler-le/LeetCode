# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(node, curr_sum):
            if not node: 
                return False
                
            if not node.left and not node.right and curr_sum + node.val == targetSum:
                return True

            if node.left and backtrack(node.left, curr_sum + node.val): 
                return True
            
            if node.right and backtrack(node.right, curr_sum + node.val):
                return True
            
            return False
        
        return backtrack(root, 0)