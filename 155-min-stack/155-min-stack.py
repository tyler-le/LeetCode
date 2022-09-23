class MinStack:
# Two stack approach:
# 1. One to store the numbers
# 2. One to store the current minimum
    def __init__(self):
        self.nums = []
        self.curr_min = [] # (curr_min, count)

    def push(self, val: int) -> None:
        self.nums.append(val)
        
        if not self.curr_min or val < self.curr_min[-1][0]: 
            self.curr_min.append([val, 1])
        elif val == self.curr_min[-1][0]:
            self.curr_min[-1][1]+=1

    def pop(self) -> None:
        popped = self.nums.pop()
        if self.curr_min and self.curr_min[-1][0] == popped: 
            self.curr_min[-1][1]-=1
        if self.curr_min[-1][1] == 0:
            self.curr_min.pop()

    def top(self) -> int:
        return self.nums[-1]
        

    def getMin(self) -> int:
        return self.curr_min[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()