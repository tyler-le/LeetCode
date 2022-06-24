# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q,res = deque(), []
        
        if not root:
            return res
        
        q.append(root)
        while q:
            level_size = len(q)
            
            for i in range(level_size):
                removed = q.popleft()
                if removed.left:
                    q.append(removed.left)
                if removed.right:
                    q.append(removed.right)
                    
                if i == level_size-1:
                    res.append(removed.val)
        return res
                        