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
        curr_sum = 0
        target = targetSum

        def dfs(node):
            nonlocal res, curr_sum, target

            if not node: return

            # pre order traversal
            curr_sum+=node.val

            if prefix_sums[curr_sum - target]:
                res+=prefix_sums[curr_sum - target]
            
            prefix_sums[curr_sum]+=1


            dfs(node.left)
            dfs(node.right)

            # remove from map
            prefix_sums[curr_sum]-=1
            curr_sum-=node.val
            
        dfs(root)
        return res