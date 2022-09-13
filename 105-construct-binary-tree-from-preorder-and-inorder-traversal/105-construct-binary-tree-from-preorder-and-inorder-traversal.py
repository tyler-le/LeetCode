# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        hmap = {}
        for index, val in enumerate(inorder):
            hmap[val] = index
            
        def helper(left, right):
            nonlocal preorder_index
            if left > right: return None
            root = TreeNode(preorder[preorder_index])
            preorder_index+=1
            
            root.left = helper(left, hmap[root.val]-1)
            root.right = helper(hmap[root.val]+1, right)
            
            return root
            
        return helper(0, len(preorder)-1)
            