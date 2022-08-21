class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.window_size = size
        self.nums = deque()
        
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) >= self.window_size: 
            self.nums.popleft()
        self.nums.append(val)
        return float(sum(self.nums)) / float(len(self.nums))
            
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)