# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, q, i = [], deque(), 0
        
        if not root:
            return res
        
        q.append(root)
        
        while q:
            curr_level = deque()
            count = len(q)
            is_even_iteration = (i%2 == 0)
            
            for j in range(count):
                popped = q.popleft()
                
                if is_even_iteration:
                    curr_level.append(popped.val)
                else:
                    curr_level.appendleft(popped.val)
                    
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                        
                
            res.append(list(curr_level))
            i+=1
                
        return res