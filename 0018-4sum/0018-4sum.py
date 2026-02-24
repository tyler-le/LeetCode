class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue

            for j in range(i+1, n):

                # Skip duplicates for the second number (j)
                # Important: check j > i+1, not j > 0
                # Why? j starts from i+1. We want the first occurrence of this value for this i.
                # If we used j > 0, we might skip a valid candidate immediately after i.
                if j > i + 1 and nums[j] == nums[j-1]: continue
                
                left = j + 1
                right = n - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum < target: 
                        left+=1
                    elif curr_sum > target: 
                        right-=1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left+=1
                        right-=1

                        # Skip duplicates **after finding a quadruplet**:
                        # Why not at the start of the while loop?
                        # - At the start, left-1 might not be part of a valid quadruplet yet
                        # - Skipping too early could miss valid quadruplets
                        # - We only want to skip repeated numbers that would produce identical results
                        while left < right and nums[left] == nums[left - 1]: left+=1
                        while left < right and nums[right] == nums[right + 1]: right-=1
        
        return res