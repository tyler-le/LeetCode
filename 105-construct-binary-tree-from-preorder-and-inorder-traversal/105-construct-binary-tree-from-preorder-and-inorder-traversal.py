# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: return None
        
        # inorder_index_map = {}
        # for index, elem in enumerate(inorder):
        #     inorder_index_map[elem] = index
        # print(inorder_index_map)
        
        root_value = preorder[0]
        root = TreeNode(root_value)
        preorder_index = inorder.index(root_value)
        
        root.left = self.buildTree(preorder[1:preorder_index+1], inorder[0:preorder_index])
        root.right = self.buildTree(preorder[preorder_index+1:], inorder[preorder_index+1:])
        
        return root