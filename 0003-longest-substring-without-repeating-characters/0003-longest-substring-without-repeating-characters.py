class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hmap = collections.defaultdict(int)
        l, res = 0, 0
        
        for r in range(len(s)):
            hmap[s[r]]+=1
            
            while hmap[s[r]] > 1:
                hmap[s[l]]-=1
                l+=1

            res = max(res, r-l+1)
        
        return res
        