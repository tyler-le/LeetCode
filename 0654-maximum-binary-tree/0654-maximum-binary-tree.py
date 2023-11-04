# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(sublist):
            if not len(sublist): return None
            maxi = max(sublist)
            maxi_pos = sublist.index(maxi)
            
            curr = TreeNode(maxi)
            curr.left = recurse(sublist[0:maxi_pos])
            curr.right = recurse(sublist[maxi_pos+1:])
            
            return curr
        
        return recurse(nums)