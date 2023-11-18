# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        res = 0
        q = deque([root])
        
        while q:
            
            res+=1
            level_size = len(q)
            
            for _ in range(level_size):
                popped = q.popleft()
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
        
        return res
            
        