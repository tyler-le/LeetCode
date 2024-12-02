class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for i, word in enumerate(sentence):

            if len(word) < len(searchWord):
                continue
            
            l, r = 0, 0
            
            while word[l] == searchWord[r]:
                l+=1
                r+=1
        
                if r == len(searchWord):
                    return i+1
            
        return -1