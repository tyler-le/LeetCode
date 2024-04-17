class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-freq, x) for x, freq in Counter(nums).items()]
        heapify(max_heap)
        res = []
        
        for _ in range(k):
            _, x = heappop(max_heap)
            res.append(x)
        
        return res