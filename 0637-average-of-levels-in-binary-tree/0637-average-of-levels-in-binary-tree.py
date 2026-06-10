# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            acc = 0

            for _ in range(level_size):
                popped = q.popleft()

                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)

                acc+=popped.val
                
            res.append(acc / level_size)

        return res

