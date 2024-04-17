# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        strings = []
        
        def dfs(node, path):
            if not node: 
                return
            
            if not node.left and not node.right:
                path.append(chr(node.val + ord('a')))
                strings.append("".join(path.copy()[::-1]))
                return

            
            dfs(node.left, path + [chr(node.val + ord('a'))])
            dfs(node.right, path + [chr(node.val + ord('a'))])
        
        dfs(root, [])
        res = strings[0]
        
        for s in strings:
            res = min(res, s)
        
        return res
            