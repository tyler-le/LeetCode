# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # (max when robbing this node, max when not robbing this node)
        def dfs(node):
            if not node: return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # rob this node
            left_no_rob = left[1]
            right_no_rob = right[1]
            rob = node.val + left_no_rob + right_no_rob

            # don't rob this node. this means we can either rob or not rob children
            left_res = max(left)
            right_res = max(right)
            no_rob = left_res + right_res
        
            return (rob, no_rob)
        
        return max(dfs(root))



            

           

            