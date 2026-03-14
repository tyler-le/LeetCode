class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        
        # K: String
        # V: Node 
        self.hmap = {}

        # DLL
        self.head = Node(0)
        self.tail = Node(math.inf)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def inc(self, key: str) -> None:
        if key not in self.hmap:
            if self.head.next.freq != 1:
                one_node = Node(1)
                self._insert_after(self.head, one_node)
                one_node.keys.add(key)
                self.hmap[key] = one_node
            else:
                one_node = self.head.next
                one_node.keys.add(key)
                self.hmap[key] = one_node

            return
        
        old_node = self.hmap[key]
        old_freq = old_node.freq
        old_node.keys.remove(key)

        if old_node.next.freq != old_freq + 1:
            new_node = Node(old_freq + 1)
            self._insert_after(old_node, new_node)            
        
        old_node.next.keys.add(key)
        self.hmap[key] = old_node.next
        if not old_node.keys: self._remove(old_node)

        

    def dec(self, key: str) -> None:
        old_node = self.hmap[key]
        old_freq = old_node.freq
        old_node.keys.remove(key)

        if old_freq > 1:
            if old_node.prev.freq != old_freq - 1:
                new_node = Node(old_freq - 1)
                self._insert_after(old_node.prev, new_node)
                new_node.keys.add(key)
                self.hmap[key] = new_node
            
            else:
                old_node.prev.keys.add(key)
                self.hmap[key] = old_node.prev
            
        else:
            del self.hmap[key]

        if not old_node.keys: self._remove(old_node)
            

    def getMaxKey(self) -> str:
        if self._is_empty(): return ""
        return next(iter(self.tail.prev.keys))
        

    def getMinKey(self) -> str:
        if self._is_empty(): return ""
        return next(iter(self.head.next.keys))

    def _insert_after(self, target, node):
        prv, nxt = target, target.next
        node.prev = prv
        node.next = nxt
        prv.next = node
        nxt.prev = node
    
    def _remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
        node.next = None
        node.prev = None
    
    def _is_empty(self):
        return self.head.next == self.tail
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()