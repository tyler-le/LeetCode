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
        
        n = len(digits)
        res = []
        
        def backtrack(i, perm):
            
            if not n: 
                return []
            
            if len(perm) == n:
                res.append("".join(perm))
                return
            
            candidates = hmap[digits[i]]
            
            for cand in candidates:
                perm.append(cand)
                backtrack(i+1, perm)
                perm.pop()
            
        backtrack(0, [])
        
        return res
            
            
            