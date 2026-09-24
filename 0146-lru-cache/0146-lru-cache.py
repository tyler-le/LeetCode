class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class DoublyLinkedList:
    def __init__(self):
        self.mru = Node(-1, -1)
        self.lru = Node(-1, -1)
        self.lru.nxt = self.mru
        self.mru.prev = self.lru
        self.size = 0

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        self.size-=1
        return node

    def insert_at_mru(self, node):
        prev = self.mru.prev
        nxt = self.mru
        prev.nxt = node
        nxt.prev = node
        node.prev = prev
        node.nxt = nxt
        self.size+=1
        return node



class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList()
        self.key_to_node = {}
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.dll.remove(node)
            self.dll.insert_at_mru(node)
            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.dll.remove(node)
            self.dll.insert_at_mru(node)
            node.val = value
            return node.val

        else:
            if self.dll.size >= self.capacity:
                deleted = self.dll.remove(self.dll.lru.nxt)
                del self.key_to_node[deleted.key]

            node = Node(key, value)
            self.key_to_node[key] = node
            self.dll.insert_at_mru(node)
            return node.val


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)