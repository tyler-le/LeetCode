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
        
        q, res = deque(), []
        if not root: return res
        q.append(root)
        
        while q:
            level_size = len(q)

            for i in range(level_size):
                popped = q.popleft()
                
                if popped.left: 
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                    
            res.append(popped.val)
            
        return res
                    
        