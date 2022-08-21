class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.window_size = size
        self.nums = deque()
        self.curr_sum = 0
        
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) >= self.window_size: 
            self.curr_sum-=self.nums[0]
            self.nums.popleft()
        self.nums.append(val)
        self.curr_sum+=val
        return float(self.curr_sum) / float(len(self.nums))
            
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)