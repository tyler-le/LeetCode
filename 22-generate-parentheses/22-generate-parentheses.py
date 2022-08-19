class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(num_open, num_closed, combination):
            if num_open == num_closed == n:
                res.append("".join(combination))
                return
                
            # choose to put open, if possible
            if num_open < n:
                combination.append('(')
                backtrack(num_open+1, num_closed, combination)
                combination.pop()
            
            # choose to put closed, if possible
            if num_open > num_closed:
                combination.append(')')
                backtrack(num_open, num_closed+1, combination)
                combination.pop()
                
        res = []    
        backtrack(0, 0, [])
        return res