class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.hmap: return False

        self.arr.append(val)
        index = len(self.arr) - 1
        self.hmap[val] = index
        return True
        
        

    def remove(self, val: int) -> bool:
        if val not in self.hmap: return False

        index = self.hmap[val]
        last_index = len(self.arr) - 1
        last_val = self.arr[last_index]

        self.arr[index], self.arr[last_index] = self.arr[last_index], self.arr[index]
        self.arr.pop()

        self.hmap[last_val] = index
        del self.hmap[val]
        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.arr) - 1)
        return self.arr[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()