class MinStack:

    def __init__(self):
        self.stack = []
        self.decreasing = [] 
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        
        if not self.decreasing or value <= self.decreasing[-1]:
            self.decreasing.append(value)
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.decreasing and self.decreasing[-1] == popped:
            self.decreasing.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.decreasing[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()