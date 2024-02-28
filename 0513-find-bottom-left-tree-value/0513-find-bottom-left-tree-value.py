# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # find height
        # return first node at that height
        q = deque([root])
        leftmost = None
        
        while q:
            level_size = len(q)
            
            for i in range(level_size):
                popped = q.popleft()
                if i == 0: leftmost = popped.val
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
            
                
        return leftmost
    