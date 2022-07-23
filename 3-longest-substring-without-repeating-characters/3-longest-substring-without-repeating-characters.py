class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while count[s[r]] > 1:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            
        return res