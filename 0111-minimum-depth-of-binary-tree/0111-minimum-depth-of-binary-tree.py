# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root, 1)])
        
        while q:
            popped_node, popped_depth = q.popleft()
            
            is_leaf = not popped_node.left and not popped_node.right
            
            if is_leaf: return popped_depth
            
            if popped_node.left:
                q.append((popped_node.left, 1+popped_depth))
            if popped_node.right:
                q.append((popped_node.right, 1+popped_depth))