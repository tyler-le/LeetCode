class RandomizedCollection:

    def __init__(self):
        self.val_to_index = defaultdict(list)
        self.arr = []
        

    def insert(self, val: int) -> bool:

        
        self.arr.append((val, len(self.val_to_index[val])))
        self.val_to_index[val].append(len(self.arr) - 1)

        if len(self.val_to_index[val]) == 1: return True
        else: return False
        
        
        

    def remove(self, val: int) -> bool:
        if not self.val_to_index[val]: return False

        index = self.val_to_index[val].pop()
        n = len(self.arr)

        self.arr[index], self.arr[n-1] = self.arr[n-1], self.arr[index]
        self.arr.pop()

        if index < len(self.arr):
            update_val, update_index = self.arr[index]
            self.val_to_index[update_val][update_index] = index

        return True

        
    

    def getRandom(self) -> int:
        index = randint(0, len(self.arr) - 1)
        return self.arr[index][0]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()