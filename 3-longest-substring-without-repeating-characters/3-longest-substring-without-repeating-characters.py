class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_char = {}
        substr_max = 0
        l, r = 0, 1
        
        if len(s) == 0:
            return substr_max
        
        if len(s) == 1:
            return 1
        
        used_char[s[l]] = 1
        while r < len(s):
            
            if s[r] in used_char and used_char[s[r]] != 0:
                print ("test")

                while used_char[s[r]] != 0:
                    used_char[s[l]] -= 1
                    l += 1
                    
            else:
                used_char[s[r]] = 1
                r += 1
                
            substr_max = max(substr_max, r-l)
                
        return substr_max
        