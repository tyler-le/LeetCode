class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # max heap of fixed-size k
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)
                    

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
        else:
            # only add elements bigger 
            if val > self.min_heap[0]:
                heappop(self.min_heap)
                heappush(self.min_heap, val)
        
        return self.min_heap[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)