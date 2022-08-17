class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.pos = dict()

    def insert(self, val: int) -> bool:
        if val in self.pos: return False

        # add to end of list
        self.vals.append(val)
        
        # mark pos in map (val : index)
        self.pos[val] = len(self.vals)-1
        
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.pos: return False
        
        # update pos map prior to swap 
        self.pos[self.vals[-1]] = self.pos[val]
        
        # swap last elem with position of val
        val_index, last_index = self.pos[val], -1        
        self.vals[val_index], self.vals[last_index] = self.vals[last_index], self.vals[val_index]

        # delete val from map
        del self.pos[val]
        
        # delete val from vals
        self.vals.pop()

        return True

    def getRandom(self) -> int:
        return self.vals[randint(0, len(self.vals)-1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()