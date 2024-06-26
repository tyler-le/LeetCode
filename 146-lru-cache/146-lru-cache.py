class Node:
    # Construct Doubly LL
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity, self.cache = capacity, {} # key : node
        
        # Create LRU and MRU nodes
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        
        # Connect LRU and MRU pointers
        self.lru.next = self.mru
        self.mru.prev = self.lru
        
    # Removed a node at any position    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # Inserts a node at MRU
    def insert_at_mru(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # If in cache, remove the node and insert at MRU
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
        # If in cache, remove, update, reinsert at MRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
            self.insert_at_mru(self.cache[key])
       
        # Else create a new node and insert at MRU
        else:
            self.cache[key] = Node(key, value)
            self.insert_at_mru(self.cache[key])
            
        # If we exceed capacity, delete from LRU and dict
        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from hashmap
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)