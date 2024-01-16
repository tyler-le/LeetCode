class RandomizedSet:

    def __init__(self):
        self.hmap = {} # map num : index in array
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.hmap:
            self.list.append(val)
            self.hmap[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hmap:
            # Index of the element to be removed
            idx = self.hmap[val]

            # Swap the element with the last one in the list
            self.list[idx], self.list[-1] = self.list[-1], self.list[idx]

            # Update the index of the swapped element in the hashmap
            self.hmap[self.list[idx]] = idx

            # Remove the last element from the list and hashmap
            self.list.pop()
            del self.hmap[val]

            return True

        return False

            

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()