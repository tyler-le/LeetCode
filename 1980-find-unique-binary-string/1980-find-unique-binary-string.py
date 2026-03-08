class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)

        def backtrack(start, path):
            nonlocal nums, n
            if len("".join(path.copy())) == n:
                if "".join(path.copy()) not in nums:
                    return "".join(path.copy())
                return

            for i in range(start, n):
                return backtrack(i + 1, path + ["0"]) or backtrack(i + 1, path + ["1"])
        
        return backtrack(0, [])


