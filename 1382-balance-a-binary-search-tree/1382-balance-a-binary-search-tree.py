# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # get a sorted list
        sorted_nodes = []
        def inorder(curr):
            nonlocal sorted_nodes
            if not curr: return
            
            inorder(curr.left)
            sorted_nodes.append(curr.val)
            inorder(curr.right)
            
        # using sorted list, create BST
        res = []
        def create(sublist):
            if not sublist: return None
            if len(sublist) == 1: return TreeNode(sublist[0], None, None)
            mid = len(sublist) // 2
            
            left = create(sublist[0:mid])
            right = create(sublist[mid+1:])
            
            node = TreeNode(sublist[mid], left, right)
            
            return node
            
        inorder(root)
        return create(sorted_nodes)
        
            
    
    