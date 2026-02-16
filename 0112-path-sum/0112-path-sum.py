# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(node, curr_sum):
            print(node.val)
            if not node.left and not node.right:
                
                if curr_sum + node.val == targetSum:
                    return True
                else:
                    return False


            if node.left and backtrack(node.left, curr_sum + node.val): 
                return True
            
            if node.right and backtrack(node.right, curr_sum + node.val):
                return True
            
            return False
        
        if not root: return False
        return backtrack(root, 0)