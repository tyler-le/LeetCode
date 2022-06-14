class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        used_char = {}
        substr_max = 1
        l, r = 0, 1
    
        used_char[s[l]] = 1
                
        while r < len(s):
            
            if s[r] in used_char and used_char[s[r]] != 0:
                while used_char[s[r]] != 0:
                    used_char[s[l]] -= 1
                    l += 1
                    
            else:
                used_char[s[r]] = 1
                r += 1
                
            substr_max = max(substr_max, r-l)
                
        return substr_max
        