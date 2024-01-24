# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        
        def is_palindrome(count):
            has_one_odd = False
            
            for cnt in count.values():
                if cnt % 2 == 1:
                    if has_one_odd: return False
                    has_one_odd = True
            
            return True
        
        
        
        def dfs(node, path):
            
            nonlocal res
            
            if node is None: return
            
            path[node.val]+=1
            
            if not node.left and not node.right: res+=is_palindrome(path)
            
            dfs(node.left, path)
            dfs(node.right, path)
            
            path[node.val]-=1
            
        res = 0  
        dfs(root, defaultdict(int))
        return res