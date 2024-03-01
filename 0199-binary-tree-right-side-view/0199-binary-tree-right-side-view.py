# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # bfs from right to left, storing first node encountered
        if not root: return []
        
        res = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            
            for i in range(level_size):
                popped = q.popleft()
                if i == 0: res.append(popped.val)
                if popped.right: q.append(popped.right)
                if popped.left: q.append(popped.left)
            
        return res