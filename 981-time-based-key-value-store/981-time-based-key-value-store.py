class TimeMap(object):

    def __init__(self):
        self.hmap = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.hmap[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        TIME, VAL = 0, 1
        vals = self.hmap[key]
        if not vals: return ""
        
        low, high = 0, len(vals)-1
        
        while low <= high:
            mid = low + (high - low) // 2            

            if vals[mid][TIME] == timestamp: return vals[mid][VAL]
            elif vals[mid][TIME] > timestamp: high = mid - 1
            else: low = mid + 1
                
        return vals[high][VAL] if vals[high][TIME] <= timestamp else ""
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)