class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        
        l = 0
        res = 0
        cnt = 0
        
        for r in range(len(s)):
            
            if s[r] in vowels:
                cnt+=1
        
            while r-l+1 > k:
                if s[l] in vowels:
                    cnt-=1
                l+=1
            
            res = max(res, cnt)
            
        return min(k, res)
            