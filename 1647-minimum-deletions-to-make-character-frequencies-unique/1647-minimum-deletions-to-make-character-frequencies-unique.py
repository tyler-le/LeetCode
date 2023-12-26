class Solution:
    def minDeletions(self, s: str) -> int:      
        
        cnt = Counter(s)
        seen = set()
        res = 0
        freqs = sorted(cnt.values(), reverse = True)
        
        for f in freqs:
            while f in seen: 
                f-=1
                res+=1
            if f: seen.add(f)
            
        return res
   