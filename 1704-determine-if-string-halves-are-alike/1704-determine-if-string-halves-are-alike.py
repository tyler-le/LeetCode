class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        cnt1 = 0
        cnt2 = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i in range(n//2):
            if s[i] in vowels:
                cnt1+=1
            
        for i in range(n//2, n):
            if s[i] in vowels:
                cnt2+=1
        
        return cnt1 == cnt2
            