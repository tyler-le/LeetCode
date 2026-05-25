class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        cnt = Counter(nums)
        arr = [i * cnt[i] for i in range(max(nums) + 1)]

        @cache
        def f(index):
            if index < 0: return 0

            take = arr[index] + f(index - 2)
            skip = f(index - 1)

            return max(take, skip)

        return f(len(arr) - 1)
        
        