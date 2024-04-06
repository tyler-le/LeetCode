# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = deque([(root, None)])
        
        while q:
            level_size = len(q)
            seen = set()
            
            for _ in range(level_size):
                popped, parent = q.popleft()
                seen.add(popped)
                
                if popped.right and popped.right in seen:
                    if parent.left == popped: parent.left = None
                    elif parent.right == popped: parent.right = None
                    return root
                
                if popped.right: q.append((popped.right, popped))
                if popped.left: q.append((popped.left, popped))