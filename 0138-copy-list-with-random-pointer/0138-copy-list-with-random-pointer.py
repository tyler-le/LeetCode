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
        
        hmap = collections.defaultdict(lambda: Node(0))
        hmap[None] = None
        
        def rec(orig):

            if orig in hmap: return hmap[orig]
            
            copy = Node(orig.val)
            hmap[orig] = copy

            copy.next = rec(orig.next)
            copy.random = rec(orig.random)
            
            return copy
        
        return rec(head)