# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []

        def add_to_min_heap(val): 
            heappush(min_heap, val)
            if len(min_heap) > k:
                heappop(min_heap)
            

        # bool, size, height
        def is_perfect(node):

            if not node.left and not node.right: 
                add_to_min_heap(1)
                return (True, 1, 1)
            elif node.left and not node.right: 
                is_perfect(node.left)
                return (False, 0, 1)
            elif not node.left and node.right: 
                is_perfect(node.right)
                return (False, 0, 1)

            left_bool, left_size, left_height = is_perfect(node.left)
            right_bool, right_size, right_height = is_perfect(node.right)

            if left_bool and right_bool and left_height == right_height: 
                add_to_min_heap(left_size + right_size + 1)
                return (True, left_size + right_size + 1, left_height + 1)
            else: return (False, 0, 1)

        is_perfect(root)
        if len(min_heap) < k: return -1
        return min_heap[0]