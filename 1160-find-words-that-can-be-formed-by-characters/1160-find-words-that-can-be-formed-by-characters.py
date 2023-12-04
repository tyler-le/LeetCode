class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        res = 0
        
        for word in words:
            my_set = Counter(chars)
            flag = True
            for ch in word:
                if ch not in my_set: 
                    flag = False
                    break
                if not my_set[ch]: 
                    flag = False
                    break
                    
                my_set[ch]-=1
            
            if flag: res+=len(word)
                
        return res