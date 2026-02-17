from heapq import heappop, heappush, heappop_max, heappush_max

class MedianFinder:

    def __init__(self):
        self.left_heap = [] # max heap
        self.right_heap = [] # min heap
        

    def addNum(self, num: int) -> None:
        # insert num into one of the heaps
        if not self.left_heap or num <= self.left_heap[0]:
            heappush_max(self.left_heap, num)
        else:
            heappush(self.right_heap, num)
        
        # rebalance from left to right
        if len(self.left_heap) > len(self.right_heap) + 1:
            popped = heappop_max(self.left_heap)
            heappush(self.right_heap, popped)

        # rebalance from right to left
        elif len(self.right_heap) > len(self.left_heap):
            popped = heappop(self.right_heap)
            heappush_max(self.left_heap, popped)
        

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return self.left_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()