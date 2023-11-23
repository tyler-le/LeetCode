class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hmap[key]
        
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if arr[mid][1] < timestamp: 
                low = mid + 1
            elif arr[mid][1] > timestamp:
                high = mid - 1
            else:
                return arr[mid][0]
            
        return arr[high][0] if high >= 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)