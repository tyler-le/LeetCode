# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def diam_helper(root):
            if root is None:
                return 0    
            
            left_height = diam_helper(root.left)
            right_height = diam_helper(root.right)
            
            curr_diameter = left_height + right_height
            self.max_diameter = max(self.max_diameter, curr_diameter) 
            
            height = max(left_height, right_height) + 1
            return height
        
        diam_helper(root)
        return self.max_diameter