class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k: return False
        choices = [0] * k
        nums.sort(reverse=True)
        target = sum(nums) // k
        states = set()

        def backtrack(index):
            nonlocal target

            if index == len(nums):
                return True

            # choices [4,0,0,0] is the same as [0,0,4,0] so skip
            if tuple(sorted(choices)) in states: return False
            else: states.add(tuple(sorted(choices)))
            
            for i in range(k):
                
                if choices[i] + nums[index] > target: continue
                
                # place nums[index] in the ith bucket
                choices[i]+=nums[index]
                
                if backtrack(index + 1): return True

                choices[i]-=nums[index]

            return False
            
        return backtrack(0)
        