class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def backtrack(num_open, num_closed, curr):

            if num_closed > num_open: 
                return
        
            if num_open > n or num_closed > n:
                return
            
            if num_open == n and num_closed == n:
                res.append(curr)
                return
            
            backtrack(num_open + 1, num_closed, curr + "(")
            backtrack(num_open, num_closed + 1, curr + ")")
            
        res = []
        backtrack(0, 0, "")
        return res