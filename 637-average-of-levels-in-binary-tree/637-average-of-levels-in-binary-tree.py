# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res, q = [], deque()
        
        if not root: 
            return 0
        
        q.append(root)
        
        while q:
            level_sum, level_size = 0, len(q)
            
            for i in range(level_size):
                popped = q.popleft()
                level_sum+=popped.val
                
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                    
            level_avg = level_sum / level_size
            res.append(level_avg)
            
        return res
            
            
        