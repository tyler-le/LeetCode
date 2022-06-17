class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        l,r=0,0
        
        my_map={}
        
        while r < len(s):
            if s[r] not in my_map:
                my_map[s[r]] = 1
                r+=1
                
            else:
                res = max(res, r-l)
                while s[l] in my_map and my_map[s[r]]>0:
                    my_map[s[l]]-=1
                    l+=1
                del my_map[s[r]]
            
        return max(res, r-l)
        