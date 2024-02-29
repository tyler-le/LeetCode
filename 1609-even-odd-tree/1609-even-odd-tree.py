# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        level_parity = 0
        q = deque([root])
        
        while q:
            
            level_size = len(q)
            prev_val = -math.inf if not level_parity else math.inf
            for _ in range(level_size):
                
                popped = q.popleft()
                
                # handle even level parity (strictly increasing and odd vals)
                if not level_parity:
                    if prev_val >= popped.val or not popped.val % 2: 
                        return False
                    prev_val = popped.val
                    

                # handle odd level parity (strictly decreasing and even vals)
                else:
                    if prev_val <= popped.val or popped.val % 2: 
                        return False
                    prev_val = popped.val
                
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                
            
            level_parity = 0 if level_parity else 1
        
        return True