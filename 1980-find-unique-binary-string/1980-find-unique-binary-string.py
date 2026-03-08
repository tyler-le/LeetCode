class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)

        def backtrack(index, path):
            nonlocal nums, n

            if index == n:
                if "".join(path.copy()) not in nums:
                    return "".join(path.copy())
                return None

            for choice in "01":
                res = backtrack(index + 1, path + [choice])
                if res: return res
            
        
        return backtrack(0, [])


