class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get frequencies
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # build (frequency, elem) heap
        max_heap = []
        
        for num, freq in count.items():
            heappush(max_heap, (-freq, num))
            
        # get k most frequent
        res = []
        for i in range(k):
            popped = heappop(max_heap)
            res.append(popped[1])
            
        return res
            
        