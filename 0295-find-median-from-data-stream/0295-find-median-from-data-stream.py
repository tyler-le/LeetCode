class MedianFinder:

    def __init__(self):

        self.left_heap = [] # max heap
        self.right_heap = [] # min heap
        

    def addNum(self, num: int) -> None:
        # insert into left heap
        if self.left_heap and num <= self.left_heap[0]: 
            heappush_max(self.left_heap, num)
    
        # or insert into right heap
        else: 
            heappush(self.right_heap, num)

        # rebalance heaps

        # right side has more -> move to left
        if len(self.left_heap) < len(self.right_heap):
            heappush_max(self.left_heap, heappop(self.right_heap))

        # left side has more -> move to right
        # we keep the one extra element in the left heap
        elif len(self.left_heap) > len(self.right_heap) + 1:
            heappush(self.right_heap, heappop_max(self.left_heap))
        
    def findMedian(self) -> float:
        
        if len(self.left_heap) == len(self.right_heap):
            return (self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return self.left_heap[0]        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()