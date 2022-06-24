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
        q = deque()
        if not root:
            return
        
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
                    removed.next = None
                else:
                    removed.next = q[0]
        return root
        