class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        """ 
        find total number of subarrays 
        find number of subarrays that DON'T have all 3 chars
        then subtract the two
        """
        
        hmap, n = defaultdict(int), len(s)
        res, l, invalid_arrs = 0, 0, 0
        total_arrs = (n*(n+1)) // 2
        
        for r in range(n):
            hmap[s[r]]+=1
            
            # find a window that does not contain all three characters
            while len(hmap) == 3:
                res+=1
                hmap[s[l]]-=1
                if not hmap[s[l]]: del hmap[s[l]]
                l+=1
            
            # number of invalid subarrs that end in index r
            invalid_arrs += (r-l+1) 
            
        return total_arrs - invalid_arrs