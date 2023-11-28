class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hmap = collections.defaultdict(int)
        self.deck = deque()
        

    def get(self, key: int) -> int:
        if key not in self.hmap: return -1
        self.deck.remove(key)
        self.deck.append(key)
        return self.hmap[key]

    def put(self, key: int, value: int) -> None:
                
        if key in self.hmap:
            self.deck.remove(key)
        elif len(self.deck) == self.size:
            popped = self.deck.popleft()
            del self.hmap[popped]
        self.deck.append(key)
        self.hmap[key] = value
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)