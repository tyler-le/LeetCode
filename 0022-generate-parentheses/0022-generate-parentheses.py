class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # base case
        # - have n open and n closed parens

        # in each step, we have two choices
        # - place "(" only if num_open < n
        # - place ")" only if num_open > num_closed


        res = []

        def backtrack(path, num_open, num_closed):

            if num_open == n and num_closed == n:
                res.append("".join(path))
                return
            
            if num_open < n:
                path.append("(")
                backtrack(path, num_open+1, num_closed)
                path.pop()

            if num_open > num_closed:
                path.append(")")
                backtrack(path, num_open, num_closed+1)
                path.pop()
            


        backtrack([], 0, 0)
        return res

        