class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        
        def backtrack(i, curr):
            nonlocal res
            
            if i == len(arr): 
                if len(curr) == len(set(curr)):
                    res = max(res, len(curr))
                return


            backtrack(i+1, curr+arr[i])
            backtrack(i+1, curr)
            
        
        backtrack(0, "")
        return res