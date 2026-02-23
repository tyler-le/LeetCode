# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = -math.inf

        # return (longest path from this node)
        def dfs(node):
            nonlocal res
            if not node: return 0
            
            # only take left or right if it is positive
            # if it is negative, we might as well NOT take it
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # calculate the result of the longest multi-branch path with this node at the root
            # multi-branch means we can consider both left and right results 
            res = max(res, node.val + left + right)

            # return longest single-branch path starting at this node.
            # because parent CANNOT use both branch-paths. 
            # single-branch means we have to choose either left or right results
            return node.val + max(left, right)
        
        dfs(root)
        return res



           

            



