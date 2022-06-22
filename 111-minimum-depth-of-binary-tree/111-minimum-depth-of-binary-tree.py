# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        min_depth, q, depth_counter = sys.maxsize, deque(), 1 
        
        q.append(root)
            
        
        while q:
            level_size = len(q)
            
            for i in range(level_size):
                popped = q.popleft()
                
                if not popped.left and not popped.right:
                    min_depth = min(min_depth, depth_counter)
                    
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                    
            depth_counter+=1
            
        return min_depth
        
        
        