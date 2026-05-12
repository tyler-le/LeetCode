# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        

        def is_palindrome(freqs):
            # a string is pseudo palindromic if at least one char has odd cnt

            num_odds = 0
            for freq in freqs.values():
                num_odds+= (freq % 2)
            
            return num_odds <= 1



            


            
        res = 0
        def dfs(node, path, freqs):
            nonlocal res
            path.append(str(node.val))
            freqs[str(node.val)]+=1

            if not node.left and not node.right:

                # print(freqs)
                res+=is_palindrome(freqs.copy())
                path.pop()
                freqs[str(node.val)]-=1
                return
            
            if node.left: dfs(node.left, path, freqs)
            if node.right: dfs(node.right, path, freqs)
            path.pop()
            freqs[str(node.val)]-=1
            return
        
        dfs(root, [], defaultdict(int))
        return res