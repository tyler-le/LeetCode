class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in seen:
            if num - 1 not in seen and num in seen:
                cnt = 0
                x = num
                while x in seen:
                    cnt+=1
                    x+=1
                res = max(res, cnt)
        return res
