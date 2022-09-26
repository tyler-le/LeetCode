class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = [1,2,3,4,5,6,7,8,9]
        
        def dfs(combination, next_num):
            if sum(combination) > n or len(combination) > k: 
                return
            
            if sum(combination) == n and len(combination) == k:
                res.append(combination.copy())
                return
            
            for i in range(next_num, 9):
                combination.append(nums[i])
                dfs(combination, i+1)
                combination.pop()
            
        dfs([], 0)
        return res