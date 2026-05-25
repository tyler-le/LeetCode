class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        cnt = Counter(nums)
        arr = [i * cnt[i] for i in range(max(nums) + 1)]
        n = len(arr)
        dp = [0 for _ in range(n)]
        for index in range(n):
            take = arr[index] + ( dp[index - 2]  if index - 2 >= 0 else 0)
            skip = dp[index - 1] if index - 1 >= 0 else 0
            dp[index] = max(take, skip)

        return dp[n-1]




        cnt = Counter(nums)
        arr = [i * cnt[i] for i in range(max(nums) + 1)]
        @cache
        def f(index):
            if index < 0: return 0
            take = arr[index] + f(index - 2)
            skip = f(index - 1)
            return max(take, skip)

        return f(len(arr) - 1)
        
        