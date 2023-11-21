class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(num_open, num_closed, comb):

            if num_open == n and num_closed == n:
                res.append(comb)
                return
            
            if num_closed > num_open: return
            if num_open > n or num_closed > n: return
            
            backtrack(num_open + 1, num_closed, comb + "(")
            backtrack(num_open, num_closed + 1, comb + ")")
            
        backtrack(0, 0, "")
        return res