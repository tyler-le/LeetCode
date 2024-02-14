class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        res = []
        curr_sum = 0
        for num in nums: 
            if num % 2 == 0: curr_sum+=num
                
        for val, index in queries:
            
            
            is_even = nums[index] % 2 == 0
            if is_even: curr_sum-=nums[index]
            
            nums[index] = nums[index] + val
            
            if not nums[index] % 2: 
                curr_sum+=nums[index]
            
            res.append(curr_sum)
        
        return res
            
            
            