class RandomizedCollection:

    def __init__(self):
        # hmap {key : [arr_index]}
        # arr = [(keys, hmap_index)]
        self.hmap = defaultdict(list)
        self.arr = []

        

    def insert(self, val: int) -> bool:
        res = False
        if val not in self.hmap: res = True
        self.hmap[val].append(len(self.arr))
        self.arr.append((val, len(self.hmap[val]) - 1))
        return res
        
    def remove(self, val: int) -> bool:
        if val not in self.hmap: return False

        # find element to swap
        arr_index = self.hmap[val].pop()
        last_arr_index = len(self.arr) - 1

        deleted_key, deleted_hmap_index = self.arr[arr_index]
        swapped_key, swapped_hmap_index = self.arr[last_arr_index]

        # swap in arr
        self.arr[arr_index], self.arr[last_arr_index] = self.arr[last_arr_index], self.arr[arr_index]
        self.arr.pop()

        # delete val from map if empty
        if not len(self.hmap[deleted_key]):
            del self.hmap[deleted_key]

        # update swapped element
        if arr_index != last_arr_index:
            self.hmap[swapped_key][swapped_hmap_index] = arr_index

        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.arr) - 1)
        return self.arr[index][0]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()