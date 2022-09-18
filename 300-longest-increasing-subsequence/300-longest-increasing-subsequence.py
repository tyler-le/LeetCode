# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [1 for _ in nums]
        
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]: 
#                     dp[i] = max(dp[i], dp[j] + 1)
                    
#         return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)
                
            
