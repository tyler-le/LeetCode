# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = deque()
        res = []
        q.append(root)
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                popped = q.popleft()
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                level.append(popped.val)
            res.append(level)
            
        return res