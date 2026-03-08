class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)

        def backtrack(index, path):
            nonlocal nums, n

            if index == n:
                if "".join(path.copy()) not in nums:
                    return "".join(path.copy())
                
                return

            return backtrack(index + 1, path + ["0"]) or backtrack(index + 1, path + ["1"])
        
        return backtrack(0, [])


