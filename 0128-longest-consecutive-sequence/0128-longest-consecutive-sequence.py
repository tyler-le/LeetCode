class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res = 0
        seen = set(nums)

        for num in seen:
            if num - 1 not in seen:
                curr = 0
                while num in seen:
                    curr+=1
                    num+=1
                res = max(res, curr)

        return res