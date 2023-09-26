# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(node, lst):
            if not node: return
            inorder(node.left, lst)
            lst.append(node.val)
            inorder(node.right, lst)
            return lst
            
        
        l1 = inorder(root1, [])
        l2 = inorder(root2, [])
        
        res, p1, p2 = [], 0, 0
        if not l1 and l2: return l2
        if l1 and not l2: return l1
        
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]: 
                res.append(l1[p1])
                p1+=1
            else: 
                res.append(l2[p2])
                p2+=1
        
        if p1 == len(l1):
            res+=l2[p2:]
        else:
            res+=l1[p1:]
            
            
        
        return res
            