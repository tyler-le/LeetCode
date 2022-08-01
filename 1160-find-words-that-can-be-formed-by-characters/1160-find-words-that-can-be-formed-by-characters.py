class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        
        for word in words:
            flag, char_count = True, Counter(chars)
            
            for ch in word:
                char_count[ch]-=1
                if ch not in char_count or char_count[ch] < 0: flag = False
                    
            if flag: 
                res+=len(word)
                
        return res
            