class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_length = len(p)
        p_cntr = Counter(p)
        n = len(s)
        l = 0
        cntr = Counter()
        res = []
        
        for r in range(n):
            
            cntr[s[r]]+=1
            
            if r - l + 1 < window_length: continue
            
            # equal to window length
            if cntr == p_cntr: res.append(l)
            
            cntr[s[l]]-=1
            l+=1
            
        return res
    
            