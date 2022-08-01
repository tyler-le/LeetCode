class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_count = Counter(chars)
        
        for word in words:
            flag, ch_count = True, char_count.copy()
            word_count = Counter(word)
            for ch in word:
                if ch not in ch_count or ch_count[ch] < word_count[ch]: 
                    flag = False
                    
            if flag: 
                res+=len(word)
                
        return res
            