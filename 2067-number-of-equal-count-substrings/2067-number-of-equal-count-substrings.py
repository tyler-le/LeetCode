class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        
        # sliding window of 1*count, 2*count, ..., 26*count
        def sliding_window(width):
            l = 0 
            ans = 0
            n = len(s)
            hmap = defaultdict(int)
            
            for r in range(n):
                hmap[s[r]]+=1
                
                while r-l+1 > width:
                    hmap[s[l]]-=1
                    if not hmap[s[l]]: del hmap[s[l]]
                    l+=1
                    
                if r-l+1 == width and all(value == count for value in hmap.values()):
                    ans+=1
                    
            return ans
            
        res = 0
        for i in range(1, 27):
            res+=sliding_window(i*count) 
        return res
            