# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root, None)
        
        q = deque([(root, 1)])
        
        while q:
                        
            popped_node, popped_depth = q.popleft()

            if popped_depth == depth - 1:
                left = popped_node.left
                right = popped_node.right
                popped_node.left = TreeNode(val, left, None)
                popped_node.right = TreeNode(val, None, right)
                continue

            if popped_node.left:
                q.append((popped_node.left, popped_depth + 1))

            if popped_node.right:
                q.append((popped_node.right, popped_depth + 1))
                    
        return root