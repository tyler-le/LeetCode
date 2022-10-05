# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append(root)
        res = []
        while q:
            current_level = len(q)
            res.append(q[-1].val)
            for _ in range(current_level):
                popped = q.popleft()
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                
        return res
        
        