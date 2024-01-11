class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen, n = set(), len(nums)
        p = 0
        for i in range(n):            
            while p < n and nums[p] in seen: p+=1 
            if p >= n: return i
            nums[i] = nums[p]   
            seen.add(nums[i])
            p+=1
            
        return i+1
    
    # [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
    #                 i
    #                                p
                
            