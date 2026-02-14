class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, n = [], len(digits)

        hmap = defaultdict(str)
        hmap["2"] = ["a", "b", "c"]
        hmap["3"] = ["d", "e", "f"]
        hmap["4"] = ["g", "h", "i"]
        hmap["5"] = ["j", "k", "l"]
        hmap["6"] = ["m", "n", "o"]
        hmap["7"] = ["p", "q", "r", "s"]
        hmap["8"] = ["t", "u", "v"]
        hmap["9"] = ["w", "x", "y", "z"]

        def backtrack(index, path):
            nonlocal res, n
            # base case
            if index >= n:
                res.append("".join(path.copy()))
                return

            # recursive case
            for ch in hmap[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res