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

            # add node.val to current sum
            curr_sum+=node.val

            # check if currSum - targetSum in map.
            # if it is, then BOTH (curr_sum - targetSum) and (targetSum) EXIST in the path
            # because curr_sum = (curr_sum - targetSum) + (targetSum)
            if curr_sum - targetSum in prefix_sums:
                res+=prefix_sums[curr_sum - targetSum]
            
            # add the prefix current sum to map
            prefix_sums[curr_sum]+=1

            # backtrack on left and right subtrees
            if node.left: dfs(node.left, curr_sum)
            if node.right: dfs(node.right, curr_sum)

            # undo our choice after exploring subtrees
            prefix_sums[curr_sum]-=1
            curr_sum-=node.val
        
        dfs(root, 0)
        return res