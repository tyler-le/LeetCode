class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = set()
        n = len(nums[0])
        nums = set(nums)
        
        def backtrack(path, idx):
            nonlocal n, res
            if idx == n:
                res.add("".join(path))
                return
            
            backtrack(path + ["0"], idx+1)
            backtrack(path + ["1"], idx+1)
        
        backtrack([], 0)
        
        for x in res:
            if x not in nums: return x
        