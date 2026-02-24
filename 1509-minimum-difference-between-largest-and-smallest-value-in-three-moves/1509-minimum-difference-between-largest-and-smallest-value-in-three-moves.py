class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4: return 0

        nums.sort()

        res = math.inf

        # remove smallest 3
        res = min(res, nums[n-1] - nums[3])

        # remove largest 3
        res = min(res, nums[n - 3 - 1] - nums[0])

        # remove smallest 1 and largest 2
        res = min(res, nums[n-3] - nums[1])

        # remove smallest 2 and largest 1
        res = min(res, nums[n-2] - nums[2])

        return res




