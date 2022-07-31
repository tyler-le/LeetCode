class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # prefix sum
        res = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            res.append(prefix_sum)

        return res