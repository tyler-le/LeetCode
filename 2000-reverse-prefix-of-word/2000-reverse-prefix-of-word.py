class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        for i in range(len(word)):
            if word[i] == ch:
                rest = word[i+1:]
                rvsd = word[:i+1][::-1]
                return rvsd+rest
        return word
                