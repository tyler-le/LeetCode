class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        
        hmap = collections.defaultdict(int)
        heap = []
        ret = []
        
        # Map (Number : Frequency)
        for num in nums:
            hmap[num]+=1
            
        # Populate Heap
        for num, freq in hmap.items():
            heappush(heap, (-freq, num))
            
        # Get Top K Frequent
        for i in range(k):
            _, num = heappop(heap)
            ret.append(num)
            
        return ret
        
            
            
        
        
        
            