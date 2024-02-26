class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(["a","e","i","o","u"])
        seen_vowels = []
        res = ""
        
        for i, ch in enumerate(s):
            if ch.lower() in vowels:
                seen_vowels.append(ch)
        
        seen_vowels.sort()
        seen_vowels = deque(seen_vowels)
        
        for i in range(len(s)):
            if s[i].lower() not in vowels: res+=s[i]
            else: res+=(seen_vowels.popleft())
        
        return res
        
            