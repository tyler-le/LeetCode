class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        cnt = Counter(words)
        max_heap = [(-freq, word) for word, freq in cnt.items()]
        res = []
        heapify(max_heap)
        
        for _ in range(k):
            res.append(heappop(max_heap)[1])
        
        return res
        
        