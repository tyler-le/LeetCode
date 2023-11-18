class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = collections.defaultdict(list)
        hmap["2"] = ["a", "b", "c"]
        hmap["3"] = ["d", "e", "f"]
        hmap["4"] = ["g", "h", "i"]
        hmap["5"] = ["j", "k", "l"]
        hmap["6"] = ["m", "n", "o"]
        hmap["7"] = ["p", "q", "r", "s"]
        hmap["8"] = ["t", "u", "v"]
        hmap["9"] = ["w", "x", "y", "z"]
        
        # visited = set()
        n = len(digits)
        res = []
        
        def backtrack(i, perm):
            
            if len(perm) == n:
                res.append("".join(perm))
                return
            
            candidates = hmap[digits[i]]

            for cand in candidates:
                # visited.add(cand)
                perm.append(cand)
                backtrack(i+1, perm)
            
                # visited.remove(cand)
                perm.pop()
            
        if not n: return []
        backtrack(0, [])
        
        return res
            
            
            