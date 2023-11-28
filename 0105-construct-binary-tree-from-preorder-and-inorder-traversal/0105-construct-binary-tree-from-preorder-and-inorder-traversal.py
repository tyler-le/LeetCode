# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def rec(preord, inord):
            if not preord or not inord:
                return None

            root = TreeNode(preord[0])
            idx = inord.index(root.val)

            left_inord = inord[:idx]
            right_inord = inord[idx + 1:]
            len_left = len(left_inord)

            root.left = rec(preord[1:1 + len_left], left_inord)
            root.right = rec(preord[1 + len_left:], right_inord)

            return root
        
        return rec(preorder, inorder)