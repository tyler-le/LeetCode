class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def backtrack(path):
            nonlocal res
            if len(path) == n:
                res.append("".join(path))
                return
            
            # if prev is 0 -> can only append 1
            if path[-1] == "0":
                backtrack(path + ["1"])

            # if prev is 1 -> can append 0 or 1
            else:
                backtrack(path + ["0"])
                backtrack(path + ["1"])
            

        backtrack(["0"])
        backtrack(["1"])
        return res