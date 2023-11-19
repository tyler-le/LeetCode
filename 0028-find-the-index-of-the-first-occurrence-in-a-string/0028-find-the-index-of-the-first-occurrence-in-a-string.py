class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sliding window of size needle
        window_len = len(needle)
        l = 0
        
        for r in range(len(haystack)):
            while r - l + 1 > window_len:
                l+=1
            
            if haystack[l:r+1] == needle: return l
        
        return -1