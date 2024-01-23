class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        
        def backtrack(i, curr):
            nonlocal res
            if i >= len(arr): 
                return

            cnt = Counter(curr).values()
            if len(cnt) == len(curr):
                res = max(res, len(curr))
                
            backtrack(i+1, curr+arr[i])
            backtrack(i+1, curr)
            
        
        backtrack(-1, "")
        return res