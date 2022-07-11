# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        queue = deque()
        queue.appendleft(root)
        res = []
        
        while queue:
            level_size = len(queue)
            curr_level = []
            
            for i in range(level_size):
                removed = queue.pop()
                curr_level.append(removed.val)
                if removed.left:
                    queue.appendleft(removed.left)
                if removed.right:
                    queue.appendleft(removed.right)
                
            res.append(curr_level)
        
        return res
            
        
        