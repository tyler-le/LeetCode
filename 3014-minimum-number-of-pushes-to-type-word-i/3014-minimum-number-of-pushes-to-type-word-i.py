class Solution:
    def minimumPushes(self, word: str) -> int:
        buckets = [[] for _ in range(8)]
        hmap = defaultdict(int)
        res = 0
        
        for i in range(len(word)):
            
            idx = i%8
            buckets[idx].append(word[i])
            hmap[word[i]] = len(buckets[idx])
        
        return sum(hmap.values())