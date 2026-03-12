class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.head = Node(-math.inf)
        self.tail = Node(math.inf)
        
        self.head.next = self.tail
        self.tail.prev = self.head

        # string : Node
        self.hmap = {}


    def inc(self, key: str) -> None:

        # check if key in hmap
        if key not in self.hmap:
            
            # create a new node with freq 1
            if self._is_empty():
                new_node = Node(1)
                new_node.next = self.tail
                new_node.prev = self.head
                self.head.next = new_node
                self.tail.prev = new_node
                new_node.keys.add(key)
                self.hmap[key] = new_node

            # or insert it into head.next if the freq is 1
            elif self.head.next.freq == 1:
                self.head.next.keys.add(key)
                self.hmap[key] = self.head.next

            # key is not in map and head.next is not freq 1
            else:
                new_node = Node(1)
                new_node.next = self.head.next
                new_node.prev = self.head
                self.head.next.prev = new_node
                self.head.next = new_node
                new_node.keys.add(key)
                self.hmap[key] = new_node

            return

        # else get the node it belongs to
        
        curr_node = self.hmap[key]

        # remove the key from the node
        curr_node.keys.remove(key)

        # create or use node with freq + 1
        new_node = None
        if curr_node.next.freq == (curr_node.freq + 1):
            # the prev node has correct frequency
            new_node = curr_node.next
        else:
            # need to insert new node with correct frequency
            new_node = Node(curr_node.freq + 1)
            next_node = curr_node.next

            new_node.next = next_node
            new_node.prev = curr_node

            curr_node.next = new_node
            next_node.prev = new_node

        # insert key into new_node
        new_node.keys.add(key)

        # update hmap with new node
        self.hmap[key] = new_node

        # if the node becomes empty, remove it
        if not curr_node.keys:
             self._remove(curr_node)



    def dec(self, key: str) -> None:
        # get curr_node
        curr_node = self.hmap[key]

        # remove key from curr_node
        curr_node.keys.remove(key)

        # early exit if the freq will go to 0
        if curr_node.freq == 1:
            
            del self.hmap[key]

            if not curr_node.keys: 
                self._remove(curr_node)
                
            return

        # check freq of prev_node
        prev_node = curr_node.prev

        # if decremented, use that node
        if prev_node.freq == (curr_node.freq - 1):
            # insert key into new_node
            prev_node.keys.add(key)
            
            # update mapping
            self.hmap[key] = prev_node


        # else create a new node with proper decrement
        else:
            new_node = Node(curr_node.freq - 1)
            
            # insert key into new_node
            new_node.keys.add(key)

            # update mapping
            self.hmap[key] = new_node

            new_node.next = curr_node
            new_node.prev = prev_node

            prev_node.next = new_node
            curr_node.prev = new_node

        # if the node becomes empty, remove it
        if not curr_node.keys:
             self._remove(curr_node)


    def getMaxKey(self) -> str:
        if self._is_empty(): return ""
        return next(iter(self.tail.prev.keys))
        
        

    def getMinKey(self) -> str:
        if self._is_empty(): return ""
        return next(iter(self.head.next.keys))

    def _is_empty(self):
        return self.head.next == self.tail and self.tail.prev == self.head

    def _remove(self, node):
        prv, nxt = node.prev, node.next

        prv.next = nxt
        nxt.prev = prv

        node.prev = None
        node.next = None
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()