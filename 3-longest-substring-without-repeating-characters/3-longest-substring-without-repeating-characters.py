class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        res = 0
        count = collections.defaultdict(int)
        
        for r in range(len(s)):
            count[s[r]]+=1
            
            while count[s[r]] > 1:
                count[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
                
        return res