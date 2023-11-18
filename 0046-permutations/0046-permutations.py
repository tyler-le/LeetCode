class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, visited = [], set()
        
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for num in nums:
                if num in visited: continue
                    
                visited.add(num)
                perm.append(num)
                
                backtrack(perm)
                
                visited.remove(num)
                perm.pop()
        
        backtrack([])
        return res