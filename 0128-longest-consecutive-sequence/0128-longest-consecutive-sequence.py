class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for num in nums:
            
            if num - 1 not in seen:
                x = num
                cnt = 0
                while x in seen:
                    cnt+=1
                    x+=1
                res = max(res, cnt)
        return res