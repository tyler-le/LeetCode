class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        
        def sliding_window(k):
            if k > len(s): return 0
            l = 0
            n = len(s)
            ans = 0
            hmap = defaultdict(int)
            
            for r in range(n):
                hmap[s[r]]+=1
                    
                while r-l+1 > k:
                    hmap[s[l]]-=1
                    if not hmap[s[l]]: del hmap[s[l]]
                    l+=1
                        
                if r-l+1 == k and all(cnt == count for cnt in hmap.values()):
                    ans+=1
                    
                
            return ans
        
        res = 0
        for i in range(1, 27):
            # run sliding window of length i * count
            res+=sliding_window(i*count)
        return res