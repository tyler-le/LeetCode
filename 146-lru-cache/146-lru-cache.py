class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity, self.cache = capacity, {} # key : node
        
        self.lru = Node(0, 0)
        self.mru = Node(0,0)
        
        self.lru.next = self.mru
        self.mru.prev = self.lru
        
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert_at_mru(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_at_mru(self.cache[key])
            return self.cache[key].val
            
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert_at_mru(self.cache[key])
            
        
        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from hashmap
            lru = self.lru.next
            self.remove(lru)
            print(lru in self.cache)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)