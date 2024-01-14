class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        
        if set(cnt1.keys()) != set(cnt2.keys()): return False
        
        for c1, c2 in zip(sorted(cnt1.values()), sorted(cnt2.values())):
            if c1 != c2: return False
        
        return True