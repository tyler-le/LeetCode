"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hmap = defaultdict(lambda x : Node(0))
        
        def rec(curr):
            if not curr: return None
            if curr in hmap: return hmap[curr]
            
            copy = Node(curr.val)
            hmap[curr] = copy
            
            copy.next = rec(curr.next)
            copy.random = rec(curr.random)
            
            return copy
        
        return rec(head)
        
        