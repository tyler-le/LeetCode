from bisect import bisect_left

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
        low, high = 0, len(arr) - 1
        index = -1

        while low <= high:
            mid = (low + (high - low) // 2)

            if arr[mid][0] > timestamp:
                high = mid - 1
            elif arr[mid][0] < timestamp:
                index = mid
                low = mid + 1
            else:
                return arr[mid][1]
        
        return arr[index][1] if index != -1 else ""

        
        
