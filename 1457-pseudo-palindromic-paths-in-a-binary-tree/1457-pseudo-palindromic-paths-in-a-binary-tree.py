# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        

        def is_palindrome(freqs):

            if sum(freqs.values()) % 2:
                
                # odd palindrome (one char has odd count. rest have even counts)
                num_odds = 0
                num_evens = 0
                for freq in freqs.values():
                    if freq % 2:
                        num_odds+=1
                    else:
                        num_evens+=1
                    
                return num_odds == 1


            else:
                # even palindrome (all chars have even count)
                num_odds = 0
                num_evens = 0
                for freq in freqs.values():
                    if freq % 2:
                        num_odds+=1
                    else:
                        num_evens+=1
                    
                return num_odds == 0

        res = 0
        def dfs(node, path, freqs):
            nonlocal res
            path.append(str(node.val))
            freqs[str(node.val)]+=1

            if not node.left and not node.right:
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