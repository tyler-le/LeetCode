class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_heap = []
        self.deleted = set()
        self.counter = 0
        

    def push(self, x: int) -> None:
        # increment the counter
        self.counter+=1

        entry = (x, self.counter)

        # push into stack
        self.stack.append(entry)

        # push into heap
        heappush_max(self.max_heap, entry)
        

    def pop(self) -> int:
        # lazy delete
        self.lazy_delete("stack")

        # pop from stack
        x, index = self.stack.pop()

        # mark index as deleted
        self.deleted.add(index)

        return x
        

    def top(self) -> int:
        # lazy delete
        self.lazy_delete("stack")

        # return top
        return self.stack[-1][0]
        

    def peekMax(self) -> int:
        # lazy delete
        self.lazy_delete("max_heap")

        # return max
        return self.max_heap[0][0]
        

    def popMax(self) -> int:
        # lazy delete
        self.lazy_delete("max_heap")

        # pop from heap
        x, index = heappop_max(self.max_heap)

        # mark index as deleted
        self.deleted.add(index)

        return x

    def lazy_delete(self, _type):
        if _type == "stack":
            # pop from stack
            while self.stack and self.stack[-1][1] in self.deleted:
                self.stack.pop()

        else:
            # pop from heap
            while self.max_heap and self.max_heap[0][1] in self.deleted:
                heappop_max(self.max_heap)
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()