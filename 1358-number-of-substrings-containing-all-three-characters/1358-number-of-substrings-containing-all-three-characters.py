class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        # find total number of subarrays for length n
        # find number of subarrays that DON'T have all 3 chars
        # subtract the two
        
        hmap = defaultdict(int)
        res = 0
        l = 0
        n = len(s)
        bad_subarrs = 0
        
        for r in range(n):
            hmap[s[r]]+=1
            
            # shrink window until condition is not met
            while len(hmap) == 3:
                res+=1
                hmap[s[l]]-=1
                if not hmap[s[l]]: del hmap[s[l]]
                l+=1
            
            bad_subarrs += (r-l+1)
            
        return (n*(n+1)) // 2 - bad_subarrs