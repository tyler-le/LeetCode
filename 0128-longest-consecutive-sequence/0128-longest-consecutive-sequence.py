class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        res = 0
        
        for i in range(len(nums)):
            
            if (nums[i] - 1) not in my_set:
                
                curr = nums[i]
                count = 0
                
                while curr in my_set:
                    count+=1
                    curr+=1
                res = max(res, count)
                
        return res