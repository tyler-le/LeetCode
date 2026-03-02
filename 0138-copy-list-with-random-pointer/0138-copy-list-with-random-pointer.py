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

        # Key: orig node
        # Val: copy node
        hmap = {}


        # returns the copy node
        def dfs(node):
            nonlocal hmap

            if not node: return None

            if node in hmap: return hmap[node]

            else:
                copy = Node(node.val)
                hmap[node] = copy
                next_copy = dfs(node.next)
                random_copy = dfs(node.random)
                hmap[node].next = next_copy
                hmap[node].random = random_copy
                
                return copy
        
        return dfs(head)


