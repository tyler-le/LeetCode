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
        old_to_new = {}
        old_to_new[None] = None
        
        # first pass - create a copy of all nodes (unlinked) and map orig to new_node
        curr = head
        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            curr = curr.next
            
        # second pass - connect all the pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next
            
        return old_to_new[head]
        