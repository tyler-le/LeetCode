# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # find the difference of height of left and right subtrees.
        # repeat recursively on left and rights
        
        
        def dfs(node):

            is_balanced = True
            if not node: return [0, True]
            
            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)
                
            if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
                is_balanced = False
            
            return [1 + max(left_height, right_height), is_balanced]
        
      
        return dfs(root)[1]
        