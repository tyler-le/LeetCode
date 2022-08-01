class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_count = Counter(chars)
        
        for word in words:
            flag, ch_count = True, char_count.copy()
            
            for ch in word:
                ch_count[ch]-=1
                if ch not in ch_count or ch_count[ch] < 0: flag = False
                    
            if flag: 
                res+=len(word)
                
        return res
            