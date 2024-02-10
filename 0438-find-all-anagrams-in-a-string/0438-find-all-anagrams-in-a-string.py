class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hmap = defaultdict(int)
        p_cnt = Counter(p)
        l = 0
        n = len(s)
        k = len(p)
        res = []
        
        for r in range(n):
            hmap[s[r]]+=1
            
            while r-l+1 > k:
                hmap[s[l]]-=1
                if not hmap[s[l]]: del hmap[s[l]]
                l+=1
                
            if r-l+1 == k and hmap == p_cnt:
                res.append(l)
                
        return res
                