class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = max(nums)
        arr = [0 for _ in range(mx + 1)]

        for num, freq in cnt.items():
            arr[num] = num * freq

        

        # f(index) is the most we can earn from 0...index
        @cache
        def f(index):
            if index < 0: return 0

            # take from index i
            take = arr[index] + f(index - 2)
            

            # do not take from index i
            not_take = f(index - 1)

            return max(take, not_take)

        n = len(arr)
        return f(n-1)

