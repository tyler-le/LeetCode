# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = deque()
        q = deque([root])
        if not root: return []

        while q:
            level_size = len(q)
            sublist = []
            for _ in range(level_size):
                popped = q.popleft()
                sublist.append(popped.val)
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)

            res.appendleft(sublist)
        return list(res)


        