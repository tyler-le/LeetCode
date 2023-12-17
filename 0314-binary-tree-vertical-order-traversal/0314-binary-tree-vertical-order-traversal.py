# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        hmap = collections.defaultdict(list)
        res = []
        if not root: return []
        while q:
            node, col = q.popleft()
            hmap[col].append(node.val)
            
            if node.left: q.append((node.left, col-1))
            if node.right: q.append((node.right, col+1))
        
        for c in range(min(hmap.keys()), max(hmap.keys())+1):
            res.append(hmap[c])
            
        return res
            
            