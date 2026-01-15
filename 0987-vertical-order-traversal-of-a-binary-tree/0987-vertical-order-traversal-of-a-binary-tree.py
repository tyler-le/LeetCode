# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        # key: the column
        # value: [(row, node.val)]
        hmap = defaultdict(list)
        min_col, max_col = 0, 0
        res = []

        # (node, row, col)
        q = deque([(root, 0, 0)])

        while q:
            node, row, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            hmap[col].append((row, node.val))

            if node.left: q.append((node.left, row + 1, col - 1))
            if node.right: q.append((node.right, row + 1, col + 1))

        for i in range(min_col, max_col + 1):
            # sort first by row, second by value
            hmap[i].sort(key = lambda x : (x[0], x[1]))
            sublist = []

            for _, num in hmap[i]:
                sublist.append(num)
            
            res.append(sublist)

        return res
