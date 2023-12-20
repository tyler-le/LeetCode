class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # have a set and if len(set) < 3 then there are dupes
        
        l = 0
        counts = collections.defaultdict(int)
        res = 0
        
        for r in range(len(s)):
            counts[s[r]]+=1
            
            while r - l + 1 > 3:
                counts[s[l]]-=1
                if not counts[s[l]]: del counts[s[l]]
                l+=1
            
            if r - l + 1 == 3:
                flag = True
                for _, freq in counts.items():
                    if freq > 1: flag = False

                if flag: res+=1
        
        return res
                