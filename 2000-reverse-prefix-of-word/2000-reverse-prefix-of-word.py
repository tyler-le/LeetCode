class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        n = len(word)
        
        for i in range(n):
            c = word[i]
            if c == ch:
                return word[:i+1][::-1] + word[i+1:]
        
        return word