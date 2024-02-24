# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([(root,1)])
        seen = []
        
        while q:
            popped_node, popped_index = q.popleft()
            seen.append(popped_index)
            
            if popped_node.left:
                q.append((popped_node.left, 2*popped_index))
            if popped_node.right:
                q.append((popped_node.right, 2*popped_index + 1))
            
            
        return max(seen) - len(seen) == 0