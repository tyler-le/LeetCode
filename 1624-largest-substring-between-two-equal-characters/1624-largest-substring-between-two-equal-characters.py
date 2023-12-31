class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # map char : list of indices
        # take the min and max position of each char
        
        hmap = collections.defaultdict(list)
        res = -1
        
        for i in range(len(s)):
            hmap[s[i]].append(i)
        
        for _, indices in hmap.items():
            res = max(res, indices[-1] - indices[0] - 1)
            
        return res
            