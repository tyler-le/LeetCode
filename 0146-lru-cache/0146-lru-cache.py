class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.lru = Node(-1, -1)
        self.mru = Node(-1,-1)
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    def insert(self, node):
        prev = self.mru.prev
        node.next = self.mru
        self.mru.prev = node
        prev.next = node
        node.prev = prev


    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv


class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DLL()
        self.capacity = capacity
        self.hmap = {}
        

    def get(self, key: int) -> int:
        if key not in self.hmap: return -1
        node = self.hmap[key]
        self.dll.remove(node)
        self.dll.insert(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            self.dll.remove(node)
        
        node = Node(key, value)
        self.hmap[key] = node
        self.dll.insert(node)

        if len(self.hmap) > self.capacity:
            lru = self.dll.lru.next
            self.dll.remove(lru)
            del self.hmap[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)