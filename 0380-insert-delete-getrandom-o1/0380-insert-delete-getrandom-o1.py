class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.hmap: return False
        self.arr.append(val)
        self.hmap[val] = len(self.arr) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hmap: return False

        index = self.hmap[val]
        self.arr[index], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[index]
        self.hmap[self.arr[index]] = index
        self.arr.pop()
        del self.hmap[val]
        return True
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.arr) - 1)
        return self.arr[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()