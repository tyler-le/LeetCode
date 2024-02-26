class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        cnt = defaultdict(int)
        n = len(words)
        
        for word in words:
            for ch in word:
                cnt[ch]+=1
        
        for ch, freq in cnt.items():
            if freq % n != 0: return False
        
        return True