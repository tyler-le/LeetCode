# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        q = deque()
        q.append(root)
        res = []
        
        while q:
            level_size = len(q)
            res.append(q[-1].val)
            for i in range(level_size):
                popped = q.popleft()
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                    
        return res
        