# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        context = {"max_depth":0, "res":0}
        
        def dfs(depth, node):
            
            if not node: return
            
            if not node.left and not node.right:
                if depth == context["max_depth"]:
                    context["res"]+=node.val
                    
                elif depth > context["max_depth"]:
                    context["max_depth"] = depth
                    context["res"] = node.val
                    
                else:
                    return
                
            if node.left: dfs(depth+1, node.left)
            if node.right: dfs(depth+1, node.right)
        
        dfs(0, root)
        return context["res"]
        