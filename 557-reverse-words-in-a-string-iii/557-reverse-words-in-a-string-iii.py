class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        
        for i in range(len(words)):
            word = list(words[i])
            l, r = 0, len(word)-1
            
            while l <= r:
                word[l], word[r] = word[r], word[l]
                l+=1
                r-=1 
            words[i] = ''.join(word)
            
            
        return ' '.join(words)

        