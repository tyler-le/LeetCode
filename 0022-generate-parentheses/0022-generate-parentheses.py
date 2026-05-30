class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(num_open, num_closed, path):
            nonlocal res
            if num_open == num_closed == n:
                res.append("".join(path.copy()))
                return
            
            if num_closed > n or num_open > n:
                return

            backtrack(num_open + 1, num_closed, path + ["("])
            if num_closed < num_open:
                backtrack(num_open, num_closed + 1, path + [")"])

        backtrack(0, 0, [])
        return res