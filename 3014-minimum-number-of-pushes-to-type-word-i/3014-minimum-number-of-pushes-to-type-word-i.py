class Solution:
    def minimumPushes(self, word: str) -> int:
        # place high frequency chars in early positions
        keypad = [[] for _ in range(8)]
        hmap = defaultdict(int)
        res = 0
        cnt = Counter(word)
        
        i = 0
        for ch, freq in cnt.items():
            keypad[i % 8].append(ch)
            hmap[ch] = len(keypad[i%8])
            i = (i + 1) % 8 
            
        for ch in word:
            res+=hmap[ch]
        return res