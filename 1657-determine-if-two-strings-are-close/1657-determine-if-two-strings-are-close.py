class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        if set(word1) != set(word2): return False
        
        c1, c2 = Counter(word1), Counter(word2)
        
        for p1, p2 in zip(sorted(c1.values()), sorted(c2.values())):
            if p1 != p2: return False
        
        return True