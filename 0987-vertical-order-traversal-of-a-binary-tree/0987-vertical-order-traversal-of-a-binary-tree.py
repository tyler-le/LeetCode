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
        
        # (node, row, col)
        q = deque([(root, 0, 0)]) 

        while q:
            popped_node, popped_row, popped_col = q.popleft()
            hmap[popped_col].append((popped_row, popped_node.val))

            if popped_node.left:
                q.append((popped_node.left, popped_row + 1, popped_col - 1))
            
            if popped_node.right:
                q.append((popped_node.right, popped_row + 1, popped_col + 1))
        
        mn, mx = min(hmap.keys()), max(hmap.keys())
        res = []
        
        for col in range(mn, mx+1):
            hmap[col].sort(key = lambda x : (x[0], x[1]))
            res.append([x for _, x in hmap[col]])

        return res