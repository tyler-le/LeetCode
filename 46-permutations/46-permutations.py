class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        used_chars = set()
        permutation = []
        
        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in used_chars:
                    permutation.append(nums[i])
                    used_chars.add(nums[i])
                    
                    backtrack()
                    
                    permutation.pop()
                    used_chars.remove(nums[i])    
                    
        backtrack()       
        return res
            
        