class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = r = 0
        window_size = len(p)
        p_count, substr_count, res = Counter(p), {}, []
        
        while r < len(s):
            substr_count[s[r]] = 1 + substr_count.get(s[r], 0)
            
            while r-l+1 > window_size:
                substr_count[s[l]]-=1
                if substr_count[s[l]] == 0: 
                    del substr_count[s[l]]
                l+=1
                
            if p_count == substr_count:
                res.append(l)
                
            r+=1
            
        return res