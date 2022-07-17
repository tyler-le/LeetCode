class TrieNode:
    def __init__(self):
        self.letters = {}
        self.is_word = False
            
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.letters:
                curr.letters[ch] = TrieNode()
            curr = curr.letters[ch]
            
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            curr = node
            
            for i in range(idx, len(word)):
                if word[i] == '.':
                    for child in curr.letters.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if word[i] not in curr.letters:
                        return False
                    curr = curr.letters[word[i]]
                
            return curr.is_word
        
        return dfs(self.root, 0)
                
            
            
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)