class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # include exclude
        n = len(nums)
        res = []

        def f(index, path):
            nonlocal res
            if index == n:
                res.append(path.copy())
                return

            f(index + 1, path + [nums[index]])
            f(index + 1, path)

        f(0, [])
        return res
