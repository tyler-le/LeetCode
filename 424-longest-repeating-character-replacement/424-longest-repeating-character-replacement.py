class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, l, count = 0, 0, {}
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most_freq = max(count.values())
            
            while r-l+1 - most_freq > k:
                count[s[l]]-=1
                l+=1
                #most_freq = max(count.values())
                
            res = max(res, r-l+1)
        
        return res