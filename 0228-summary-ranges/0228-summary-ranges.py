class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        l, r, n = 0, 0, len(nums)
        res = []

        while r < n:
            l = r

            # move r until nonsequential
            while (r + 1 < n) and nums[r] + 1 == nums[r+1]:
                r+=1
            
            if r == l: res.append(f"{nums[r]}")
            else: res.append(f"{nums[l]}->{nums[r]}")

            r+=1

        return res
