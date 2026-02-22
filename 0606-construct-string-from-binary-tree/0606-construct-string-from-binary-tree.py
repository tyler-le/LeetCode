# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            # preorder traversal:
            if not node: return None
            

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return f"{node.val}({left})({right})"
            elif not left and right:
                return f"{node.val}()({right})"
            elif left and not right:
                return f"{node.val}({left})"
            else:
                return f"{node.val}"

        return dfs(root)