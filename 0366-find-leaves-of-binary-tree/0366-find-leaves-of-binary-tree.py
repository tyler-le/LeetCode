# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:


        depths = defaultdict(list)
        # get height from bottom

        def dfs(node):
            if not node: return 0
            if not node.left and not node.right:
                depths[0].append(node.val)
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            depth = 1 + max(left, right)

            depths[depth].append(node.val)
            return depth

        depth = dfs(root)
        res = []

        for i in range(depth+1):
            res.append(depths[i])
        
        return res