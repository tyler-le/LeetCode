# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxi = -float('inf')
        
        def rec(root):
            nonlocal maxi
            
            # base case
            if not root: return 0
        
            # recurse
            left = max(rec(root.left), 0)
            right = max(rec(root.right), 0)
            
            # calculate result for current tree
            maxi = max(maxi, left + right + root.val)
            
            return max(left+root.val, right+root.val)
            
                    
        
        rec(root)
        return maxi
        
            
            