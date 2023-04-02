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
        
        q, out = deque(), []
        q.appendleft(root)
        
        while q:
            level_size = len(q)
            curr_level = []
            for i in range(level_size):
                popped = q.pop()
                curr_level.append(popped.val)
                if popped.left: q.appendleft(popped.left)
                if popped.right: q.appendleft(popped.right)
            out.append(curr_level)
            
        return out
                

        