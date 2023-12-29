# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return None
        
        q = deque([root])
        res = []
        
        while q:
            level_size = len(q)
            
            for i in range(level_size):
                popped = q.popleft()
                if i == level_size - 1: res.append(popped.val)
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
        
        return res