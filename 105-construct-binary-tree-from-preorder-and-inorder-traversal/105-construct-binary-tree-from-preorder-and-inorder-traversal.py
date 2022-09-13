# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            
            nonlocal preorder_index
            
            if left > right: return None
            root_value = preorder[preorder_index]
            preorder_index+=1
            root = TreeNode(root_value)
            
            inorder_index = inorder_index_map[root_value]
            
            root.left = helper(left, inorder_index-1)
            root.right = helper(inorder_index+1, right)
            
            return root
            
            
            
            
        
        
        # get indices of each element in inorder for quick access
        inorder_index_map = {}
        for index, elem in enumerate(inorder):
            inorder_index_map[elem] = index
            
        preorder_index = 0
        return helper(0, len(preorder)-1)