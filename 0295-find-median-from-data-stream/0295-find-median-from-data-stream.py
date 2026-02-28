from heapq import heappush, heappop, heappush_max, heappop_max

class MedianFinder:

    def __init__(self):
        self.left_heap = [] # max heap
        self.right_heap = [] # min_heap
        

    def addNum(self, num: int) -> None:
        # initially add to heap

        # add to right heap
        if self.left_heap and num > self.left_heap[0]:
            heappush(self.right_heap, num)
        
        # else add to left heap
        else:
            heappush_max(self.left_heap, num)

        # rebalance - right heap too big
        if len(self.right_heap) > len(self.left_heap):
            heappush_max(self.left_heap, heappop(self.right_heap))

        # rebalance - left heap too big
        elif len(self.left_heap) > len(self.right_heap) + 1:
            heappush(self.right_heap, heappop_max(self.left_heap))
        

    def findMedian(self) -> float:

        # odd length -> top of left heap
        if len(self.left_heap) != len(self.right_heap):
            return self.left_heap[0]

        # even length -> top of both / 2
        else:
            return (self.left_heap[0] + self.right_heap[0]) / 2
        
        