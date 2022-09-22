class Node(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):

    def __init__(self):
        self.root = Node()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for w in word:
            if w not in curr.children: 
                curr.children[w] = Node()
            curr = curr.children[w]
            
        curr.is_word = True
                
            
        
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for w in word:
            if w not in curr.children: return False
            curr = curr.children[w]
        return curr.is_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for p in prefix:
            if p not in curr.children: return False
            curr = curr.children[p]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)