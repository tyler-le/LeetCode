# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)]) # (node, index)
        res = 0

        while q:
            level_size = len(q)
            min_index, max_index = math.inf, -math.inf
            for _ in range(level_size):
                popped_node, popped_index = q.popleft()
                min_index = min(min_index, popped_index)
                max_index = max(max_index, popped_index)

                if popped_node.left: q.append((popped_node.left, 2*popped_index + 1))
                if popped_node.right: q.append((popped_node.right, 2*popped_index + 2))

            res = max(res, max_index - min_index + 1)
            
        return res


