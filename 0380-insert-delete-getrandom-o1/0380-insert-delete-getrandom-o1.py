class RandomizedSet:

    def __init__(self):
        self.hmap = defaultdict(int)
        

    def insert(self, val: int) -> bool:
        res = False
        if val not in self.hmap: res = True
        self.hmap[val]+=1
        return res
        

    def remove(self, val: int) -> bool:
        res = False
        if val in self.hmap:
            res = True
            del self.hmap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(list(self.hmap.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()