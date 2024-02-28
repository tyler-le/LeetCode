# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # find height
        # return first node at that height
        
        max_height = 0
        
        def get_height(node):
            nonlocal max_height
            if not node: return 0
            
            left = get_height(node.left)
            right = get_height(node.right)
            curr_height = 1 + max(left, right)
            
            max_height = max(max_height, curr_height)
            
            return curr_height
        
        get_height(root)
        
        # (node, curr_height)
        q = deque([(root, 1)])
        
        while q:
            popped_node, popped_height = q.popleft()
            if popped_height == max_height: return popped_node.val
            
            if popped_node.left: q.append((popped_node.left, popped_height+1))
            if popped_node.right: q.append((popped_node.right, popped_height+1))
                
    