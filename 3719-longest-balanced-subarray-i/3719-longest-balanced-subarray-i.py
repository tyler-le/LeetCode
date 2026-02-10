class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range (n):
            evens = set()
            odds = set()
            for j in range(i, n):
                num = nums[j]
                if num % 2: odds.add(num)
                else: evens.add(num)
                
                if len(odds) == len(evens): res = max(res, j - i + 1)
        
        return res