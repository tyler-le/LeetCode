# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = None
        while q:
            q_len = len(q)

            for i in range(len(q)):
                popped = q.popleft()

                if not i: res = popped

                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)

        return res.val
