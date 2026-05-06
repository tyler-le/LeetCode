from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # K: key
        # V: (timestamp, val)
        self.hmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([timestamp, value])
        return
        
        

    def get(self, key: str, timestamp: int) -> str:

        arr = self.hmap[key]
        index = bisect_right(arr, timestamp, key = lambda x : x[0]) - 1
 
        if index < 0: return ""

        return arr[index][1]

        
