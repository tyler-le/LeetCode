class Solution(object):
    def topKFrequent(self, nums, k):
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # (frequency, num)
        heap = []
        res = []
        count = collections.defaultdict(int)
        
        for num in nums:
            count[num]+=1   
        
        for num, freq in count.items():
            heap.append((-freq, num))
        
        heapify(heap)
        
        for i in range (k):
            _, popped = heappop(heap)
            res.append(popped)
        
        return res
            
        