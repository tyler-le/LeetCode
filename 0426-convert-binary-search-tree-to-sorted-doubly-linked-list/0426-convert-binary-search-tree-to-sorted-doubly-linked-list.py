"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first = last = None
        if not root: return None
        
        def inorder(root):
            nonlocal first, last
            
            if not root: return
            
            inorder(root.left)
            
            # If a previous node has been traversed, connect the pointers
            if last:
                last.right = root
                root.left = last
              
            # elif previous node has not been traversed, so this must be the first node
            else:
                first = root
                
            # set the previous node to current node and traverse right
            last = root
            
            inorder(root.right)
        
        inorder(root)
        
        # connect the ends of the Doubly LL
        last.right = first
        first.left = last
        
        return first
        