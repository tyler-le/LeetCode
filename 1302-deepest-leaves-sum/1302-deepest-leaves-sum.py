# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # bfs solution , adding all nodes in the last layer
        ret = 0
        q = deque([root])
        
        while q:
            ret = 0
            layer_size = len(q)
            
            for _ in range(layer_size):
                popped = q.popleft()
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                ret+=popped.val
                
        return ret
    
        
        
        