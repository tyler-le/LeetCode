class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, n, res = 0, len(nums), []

        for r in range(1, n):
            # add to the window
            if nums[r] - 1 == nums[r-1]:
                continue
            else:
                if r-l == 1: res.append(f"{nums[l]}")
                else: res.append(f"{nums[l]}->{nums[r-1]}")
                l = r

        if l == n-1: res.append(f"{nums[l]}")
        else: res.append(f"{nums[l]}->{nums[n-1]}")
        return res

