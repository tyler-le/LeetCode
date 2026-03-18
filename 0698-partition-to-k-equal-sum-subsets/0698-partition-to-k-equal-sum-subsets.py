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
            
            # if we made it to the end, return true
            if index == len(nums): return True

            # if we've seen this path in the past
            # it must have not hit the 'return true' path
            # so immediately return false
            if tuple(sorted(choices)) in seen: return False
            else: seen.add(tuple(sorted(choices)))


            # go through each bucket and put nums[index] in that bucket
            for i in range(k):
                num = nums[index]
                if choices[i] + num > target: continue

                choices[i]+=num
                if backtrack(index + 1): return True
                choices[i]-=num

            return False

        return backtrack(0)