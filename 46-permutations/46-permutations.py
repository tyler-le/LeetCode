class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        
        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy()) 
                return
                
            for num in nums:
                if num in visited: continue
                visited.add(num)
                perm.append(num)
                backtrack()
                perm.pop()
                visited.remove(num)
            
        perm = []
        backtrack()
        return res