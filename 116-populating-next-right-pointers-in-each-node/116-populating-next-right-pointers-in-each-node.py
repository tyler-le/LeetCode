"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        q = deque()
        q.append(root)
        
        while q:
            level_size = len(q)
            for i in range(level_size):
                popped = q.popleft()
                popped.next = None if (i == level_size-1) else q[0]
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                
                
                
        return root
                