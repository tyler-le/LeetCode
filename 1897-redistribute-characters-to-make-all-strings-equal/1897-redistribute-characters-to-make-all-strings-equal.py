class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        # the trick is to make sure count(each char) % n == 0
        
        freqs = [0] * 26
        
        for word in words:
            for ch in word:
                freqs[ord(ch) - ord("a")]+=1
        
        for f in freqs:
            if f and f % len(words): return False
        
        return True