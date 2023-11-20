# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(sublist):
            if not sublist: return None
            val, rest = sublist[0], sublist[1:]
            
            smaller = [x for x in rest if val > x]
            bigger = [x for x in rest if val < x]
            
            node = TreeNode(val)
            node.left = dfs(smaller)
            node.right = dfs(bigger)
            
            return node
        
        return dfs(preorder)
            
        
            
            