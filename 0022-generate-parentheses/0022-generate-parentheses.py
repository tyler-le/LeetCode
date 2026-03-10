class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, num_open, num_closed):
            nonlocal res 

            if num_open == n and num_closed == n:
                res.append("".join(path.copy()))
                return
            
            if num_open < n: 
                backtrack(path + ["("], num_open + 1, num_closed)

            if num_open > num_closed:
                backtrack(path + [")"], num_open, num_closed + 1)
        
        backtrack([], 0, 0)
        return res