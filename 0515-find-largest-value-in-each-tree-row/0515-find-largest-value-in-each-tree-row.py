# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        
        q = deque([root])
        
        while q:
            level_size = len(q)
            row_max = -math.inf
            
            for _ in range(level_size):
                popped = q.popleft()
                row_max = max(row_max, popped.val)
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                    
            res.append(row_max)
        
        return res