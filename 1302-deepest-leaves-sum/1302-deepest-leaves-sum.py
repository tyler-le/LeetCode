# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # deepest leaves are in the last layer of BFS
        
        q = [root]
        
        while q:
            level_sum, level_size = 0, len(q)

            for i in range(level_size):
                popped = q.pop(0)
                level_sum+=popped.val
                
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                    
        return level_sum
                
        