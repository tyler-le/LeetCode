class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i in range(n//2):
            if s[i] in vowels:
                cnt1[s[i]]+=1
            
            
        for i in range(n//2, n):
            if s[i] in vowels:
                cnt2[s[i]]+=1
        
        return sum(cnt1.values()) == sum(cnt2.values())
            