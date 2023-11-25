class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
    
        arr = [ch for ch in s if ch.lower() in vowels]
                
        s = list(s)
        
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s[i] = arr.pop()
        
        return "".join(s)