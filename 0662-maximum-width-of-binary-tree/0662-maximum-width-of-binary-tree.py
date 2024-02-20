# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bfs but adding nulls
        
        res = 0
        q = deque([(root, 0)])
        
        while q:
            level_size = len(q)
            mn, mx = math.inf, -math.inf
            
            for _ in range(level_size):
                popped, col = q.popleft()
                mn = min(mn, col)
                mx = max(mx, col)
                if popped.left: 
                    q.append((popped.left, 2*col))
                if popped.right: 
                    q.append((popped.right, 2*col + 1))
            res = max(res, mx - mn + 1)
        
        return res

            