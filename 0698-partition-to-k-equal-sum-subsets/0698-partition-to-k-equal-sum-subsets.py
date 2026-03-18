class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum = sum(nums)
        if _sum % k: return False
        target = _sum // k
        choices = [0] * k
        nums.sort(reverse = True)
        seen = set()

        def backtrack(index):
            nonlocal target, choices
            
            if index == len(nums): return True

            if tuple(sorted(choices)) in seen: return False
            else: seen.add(tuple(sorted(choices)))

            for i in range(k):
                num = nums[index]
                if choices[i] + num > target: continue

                choices[i]+=num
                if backtrack(index + 1): return True
                choices[i]-=num

            return False

        return backtrack(0)