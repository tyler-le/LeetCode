class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        
        def backtrack(i, curr):
            nonlocal res
            # Adjusted base case for stopping recursion
            if i == len(arr): 
                cnt = Counter(curr).values()
                if len(cnt) == len(curr):
                    res = max(res, len(curr))
                return

            # Include the current string in the set
            backtrack(i + 1, curr + arr[i])
            # Do not include the current string in the set
            backtrack(i + 1, curr)
            
        backtrack(0, "")
        return res
