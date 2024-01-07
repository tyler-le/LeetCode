# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bfs with (node, column) tuples
        
        q = deque([(root, 0)])
        res = 0
        
        while q:
            level_size = len(q)
            mini, maxi = float("inf"), -float("inf")
            
            for _ in range(level_size):
                popped, col = q.popleft()
                mini = min(mini, col)
                maxi = max(maxi, col)
                
                if popped.left: q.append((popped.left, 2*col))
                
                if popped.right: q.append((popped.right, 2*col + 1))
            
            res = max(res, maxi - mini + 1)
                
                
        return res
                
                
            
        return res