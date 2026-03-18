class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum = sum(nums)
        if _sum % k: return False
        target = _sum // k
        choices = [0] * k
        nums.sort(reverse = True)
        states = {}

        def backtrack(index):
            nonlocal target, choices
            
            if index == len(nums):
                return True

            x = tuple(sorted(choices))
            if x in states: 
                return states[x]

            for i in range(k):
                num = nums[index]
                if choices[i] + num > target: continue

                choices[i]+=num
                if backtrack(index + 1): 
                    states[x] = True
                    return True
                choices[i]-=num


            states[tuple(choices)] = False
            return False

        return backtrack(0)