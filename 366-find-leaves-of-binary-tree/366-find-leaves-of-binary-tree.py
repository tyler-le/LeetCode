# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        heights = collections.defaultdict(list)
        
        def dfs(node):
            if not node: return 0
            height = 1 + max(dfs(node.left), dfs(node.right))
            heights[height].append(node.val)
            return height
                
        dfs(root)
        res = [vals for vals in heights.values()]
        return res
            
    