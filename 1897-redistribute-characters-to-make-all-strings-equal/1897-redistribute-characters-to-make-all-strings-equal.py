class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        chars = defaultdict(int)
        
        for word in words:
            for ch in word:
                chars[ch]+=1
        
        for ch in chars.values():
            if ch % len(words): return False
        
        return True