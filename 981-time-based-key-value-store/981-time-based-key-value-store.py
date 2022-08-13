class TimeMap:
# key:array of values, perform binary search
    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        KEY, TIME = 0, 1
        if key not in self.hmap: return ""
        
        vals = self.hmap[key]
        
        low, high = 0, len(vals)-1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if vals[mid][TIME] == timestamp: return vals[mid][KEY]
            elif vals[mid][TIME] < timestamp: low = mid + 1
            else: high = mid - 1

        return vals[high][KEY] if vals[high][TIME] <= timestamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)