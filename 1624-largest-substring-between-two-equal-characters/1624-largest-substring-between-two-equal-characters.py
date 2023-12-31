class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # map char : first index appeared
        
        hmap = collections.defaultdict(int)
        res = -1
        
        for i in range(len(s)):
            if s[i] in hmap:
                res = max(res, i - hmap[s[i]] - 1)
            else:
                hmap[s[i]] = i
        
        return res
        
        
            