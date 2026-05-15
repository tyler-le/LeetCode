class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        base = [i for i in range(1, mx+1)] + [mx]

        return Counter(nums) == Counter(base)
