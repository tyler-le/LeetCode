class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_heap = []
        self.index = 0
        self.deleted = set()
        

    def push(self, x: int) -> None:
        # increment the counter
        self.index+=1

        elem = (x, self.index)

        # push (val, index) into stack
        self.stack.append(elem)

        # push (val, index) into heap
        heappush_max(self.max_heap, elem)

        

    def pop(self) -> int:

       # lazy_delete()
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()


        # pop (val, index) from stack
        x, index = self.stack.pop()

        # mark index as deleted
        self.deleted.add(index)

        return x
        

    def top(self) -> int:

        # lazy_delete()
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()

        # get top of stack
        return self.stack[-1][0]
        

    def peekMax(self) -> int:
        # lazy_delete()
        while self.max_heap and self.max_heap[0][1] in self.deleted:
            heappop_max(self.max_heap)

        # return top
        return self.max_heap[0][0]
        

    def popMax(self) -> int:
        # lazy_delete()
        while self.max_heap and self.max_heap[0][1] in self.deleted:
            heappop_max(self.max_heap)

        # pop from heap
        x, index = heappop_max(self.max_heap)

        # mark index as deleted
        self.deleted.add(index)

        return x
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()