# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        
        if not root: return res

        while q:
            q_size = len(q)
            sublist = []
            
            for i in range(q_size):
                popped = q.popleft()
                sublist.append(popped.val)
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                    
            res.append(sublist)
        
        return res
            
        