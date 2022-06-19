class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        count = {}
        l = r = 0
        
        while r < len(s):
            count[s[r]] = 1+count.get(s[r],0)
            most_frequent = max(count.values())
            num_replacements = (r-l+1) - most_frequent
            
            if num_replacements > k:
                count[s[l]]-=1
                l+=1
                
            max_len = max(r-l+1, max_len)
            r+=1
            
        return max_len
        