# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        arr = []

        def inorder(node):
            nonlocal arr
            if not node: return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        def build_tree(low, high):
            if low > high: return None

            mid = (high + low) // 2
            root = TreeNode(arr[mid], None, None)

            root.left = build_tree(low, mid - 1)
            root.right = build_tree(mid + 1, high)

            return root


        inorder(root)
        return build_tree(0, len(arr) - 1)