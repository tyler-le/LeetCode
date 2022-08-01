class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_count = Counter(chars)
        
        for word in words:
            flag = True
            word_count = Counter(word)
            for ch in word:
                if ch not in char_count or char_count[ch] < word_count[ch]: 
                    flag = False
                    
            if flag: 
                res+=len(word)
                
        return res
            