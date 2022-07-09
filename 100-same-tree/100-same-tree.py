# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        stack = deque()
        stack.append((p,q))
        
        while stack:
            p, q = stack.popleft()
            if p is None and q is None:
                continue
                
            if (p is None and q is not None) or (p is not None and q is None):
                return False
            
            if p.val != q.val:
                return False
            
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        return True
        