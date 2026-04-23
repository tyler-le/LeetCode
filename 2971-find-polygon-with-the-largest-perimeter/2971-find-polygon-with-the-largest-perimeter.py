class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        acc = 0
        prefix_sum = []
        res = -1
        n = len(nums)

        for num in nums:
            acc+=num
            prefix_sum.append(acc)

        for i in range(1, n-1):
            if prefix_sum[i] > nums[i+1]:
                res = max(res, prefix_sum[i] + nums[i+1])

        return res
