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
                
                if popped.right in seen:
                    # this is the tricky part -- 
                    # from example 1 -- 
                    # we need to remove the "2" node
                    # we can do this by looking at the parent ("1")
                    # and checking the parents left and right
                    # and look for "popped" and set it to None
                    if parent.left == popped: parent.left = None
                    elif parent.right == popped: parent.right = None
                    return root
                
                if popped.right: q.append((popped.right, popped))
                if popped.left: q.append((popped.left, popped))