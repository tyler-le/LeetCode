class Trie:

    class Node:
        def __init__(self):
            self.letters = {}
            self.is_word = False
    
    def __init__(self):
        self.root = self.Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.letters:
                curr.letters[ch] = self.Node()
            curr = curr.letters[ch]
            
        curr.is_word = True
        
            
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.letters:
                return False
            curr = curr.letters[ch]
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.letters:
                return False
            curr = curr.letters[ch]
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)