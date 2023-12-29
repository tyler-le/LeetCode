# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        maxi = -float(inf)
        q = deque([root])
        res = 0
        
        while q:
            level_size = len(q)
            sumi = 0
            
            for _ in range(level_size):
                popped = q.popleft()
                sumi+=popped.val
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
            
            if sumi > maxi: 
                maxi = sumi
                res = level
            level+=1
                
        return res
            