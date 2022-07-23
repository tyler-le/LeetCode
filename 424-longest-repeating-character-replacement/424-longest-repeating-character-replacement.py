class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r], 0)
            most_freq = max(count.values())
            num_replacements = (r-l+1) - most_freq
            
            while num_replacements > k:
                count[s[l]] -= 1
                l+=1
                most_freq = max(count.values())
                num_replacements = (r-l+1) - most_freq
            res = max(res, r-l+1)
            
        return res