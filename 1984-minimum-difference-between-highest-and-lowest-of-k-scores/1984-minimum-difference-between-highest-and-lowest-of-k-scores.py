class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
            sublist = nums[i:i + k]
            mini, maxi = min(sublist), max(sublist)
            diff = abs(mini - maxi)
            res = min(res, diff)
            
        return res if res != float('inf') else 0