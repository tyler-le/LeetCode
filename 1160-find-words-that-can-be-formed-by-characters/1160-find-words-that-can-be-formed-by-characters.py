class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            flag = True
            char_count = Counter(chars)
            for ch in word:
                
                if ch not in char_count: 
                    flag = False
                char_count[ch]-=1
                if char_count[ch] < 0:
                    flag = False
            if flag: 
                res+=len(word)
                print(word)
        return res
            