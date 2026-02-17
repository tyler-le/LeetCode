# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        res = 0

        def dfs(node, curr_sum):
            nonlocal prefix_sums, res
            if not node: return 0
            curr_sum+=node.val

            if curr_sum - targetSum in prefix_sums:
                res+=prefix_sums[curr_sum - targetSum]
            
            prefix_sums[curr_sum]+=1

            if node.left: dfs(node.left, curr_sum)
            if node.right: dfs(node.right, curr_sum)

            prefix_sums[curr_sum]-=1
            # curr_sum-=node.val
        
        dfs(root, 0)
        return res