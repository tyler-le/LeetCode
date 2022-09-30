class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        max_heap = [(-cnt, item) for item, cnt in count.items()]
        res = []
        
        heapify(max_heap)       
        
        for _ in range(k):
            res.append(heappop(max_heap)[1])
        
        return res
            