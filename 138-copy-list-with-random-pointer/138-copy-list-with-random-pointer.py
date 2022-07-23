"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old2new = {None:None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            old2new[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            old2new[curr].next = old2new[curr.next]
            old2new[curr].random = old2new[curr.random]
            curr = curr.next
        
        return old2new[head]
        