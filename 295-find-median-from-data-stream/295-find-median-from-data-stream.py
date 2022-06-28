class MedianFinder(object):

    def __init__(self):
        # max-heap, min-heap
        self.first_half, self.second_half = [], []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # num belongs in first_half
        if not self.first_half or -self.first_half[0] >= num:
            heappush(self.first_half, -num)
            
        # num belongs in second half
        else:
            heappush(self.second_half, num)
            
            
        # balance out the heaps
#         if len(self.first_half) > len(self.second_half) + 1:
#             removed = heappop(self.first_half)
#             heappush(self.second_half, removed)
            
#         elif len(self.first_half) < len(self.second_half):
#             removed = -heappop(self.second_half)
#             heappush(self.first_half, removed)
            
        if len(self.first_half) > len(self.second_half) + 1:
            heappush(self.second_half, -heappop(self.first_half))
        elif len(self.first_half) < len(self.second_half):
            heappush(self.first_half, -heappop(self.second_half))
            
        
            
            
        

    def findMedian(self):
        """
        :rtype: float
        """
        if ( len(self.first_half) + len(self.second_half) ) % 2 == 0:
            return (-self.first_half[0] / 2.0) + (self.second_half[0] / 2.0)
        else:
            return -self.first_half[0] / 1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()