# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        q,res=deque(),[]
        
        if not root:
            return res
        
        q.append(root)
        
        while q:
            level_size, curr_level = len(q), []
            
            for i in range(level_size):
                removed = q.popleft()
                curr_level.append(removed.val)
                
                if removed.left:
                    q.append(removed.left)
                if removed.right:
                    q.append(removed.right)
                
            res.insert(0, curr_level)
            
        return res