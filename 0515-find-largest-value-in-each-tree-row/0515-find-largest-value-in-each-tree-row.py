# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        q = deque([root])
        
        while q:
            
            level_size = len(q)
            curr_max = -math.inf
            
            for _ in range(level_size):
                popped = q.pop()
                if popped.left: q.appendleft(popped.left)
                if popped.right: q.appendleft(popped.right)
                curr_max = max(curr_max, popped.val)
                
            res.append(curr_max)
        
        return res
                