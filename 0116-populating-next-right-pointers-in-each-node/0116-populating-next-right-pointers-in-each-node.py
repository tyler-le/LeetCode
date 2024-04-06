"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root: return None
        q = deque([root])
        
        while q:
            level_size = len(q)
            prev = None
            
            for _ in range(level_size):
                popped = q.popleft()
                popped.next = prev
                prev = popped
                
                if popped.right: q.append(popped.right)
                if popped.left: q.append(popped.left)
        
        return root
                