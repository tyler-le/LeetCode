class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer + set
        if s == "":
            return 0
        
        l = 0
        hmap = collections.defaultdict(int)
        res = 0
        
        for r in range(len(s)):
            curr = s[r]
            hmap[curr]+=1
            
            while hmap[curr] > 1:
                # keep incrementing left pointer until hmap[curr] == 0
                hmap[s[l]]-=1
                l+=1
                
            res = max(res, r-l+1)
        
        return max(res, r-l+1)
                
            
            
            
            