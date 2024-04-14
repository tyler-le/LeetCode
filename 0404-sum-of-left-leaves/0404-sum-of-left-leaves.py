# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, False)])
        res = 0
        
        while q:
            level_size = len(q)
            
            for _ in range(level_size):
                popped, is_left = q.popleft()
                
                is_leaf = not popped.left and not popped.right
                
                if is_leaf and is_left: 
                    res+=popped.val
                
                if popped.left:
                    q.append((popped.left, True))
                if popped.right:
                    q.append((popped.right, False))
        
        return res