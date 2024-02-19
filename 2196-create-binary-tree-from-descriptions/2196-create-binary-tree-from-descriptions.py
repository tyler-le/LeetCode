# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hmap = {}
        seen = set()
        
        for p, c, is_left in descriptions:
            if p not in hmap: hmap[p] = TreeNode(p)
            if c not in hmap: hmap[c] = TreeNode(c)
                
            if is_left: hmap[p].left = hmap[c]
            else: hmap[p].right = hmap[c]
                
            seen.add(c)
        
        for p, _, _ in descriptions:
            if p not in seen: return hmap[p]
