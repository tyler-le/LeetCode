class RandomizedCollection:

    def __init__(self):

        # (val, idx) where idx is the pos in self.arr
        # we use the idx here to map the pos in self.arr
        self.val_to_index = defaultdict(list)

        # (val, idx) where idx is the pos in self.val_to_index[val]
        # we use the idx here to map to the pos in self.val_to_index[val]
        self.arr = []
        

    def insert(self, val: int) -> bool:

        # insert (val, index) at the end of arr
        # where index is the position in val_to_idx[val]
        self.arr.append((val, len(self.val_to_index[val])))

        # insert idx in self.val_to_index to point to the position in self.arr
        self.val_to_index[val].append(len(self.arr) - 1)

        # if first time, return True
        if len(self.val_to_index[val]) == 1: return True
        else: return False
        
        
        

    def remove(self, val: int) -> bool:
        if not self.val_to_index[val]: return False

        # get the position of val in self.arr using self.val_to_index
        index = self.val_to_index[val].pop()
        n = len(self.arr)

        # swap val with the last element
        self.arr[index], self.arr[n-1] = self.arr[n-1], self.arr[index]

        # remove val by popping
        self.arr.pop()

        # if we did not remove the last element, update swapped element tables
        if index < len(self.arr):
            # update the item that was swapped and still remains
            update_val, update_index = self.arr[index]

            # update self.val_to_index[update_val] 
            # to point to the correct pos in self.arr
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