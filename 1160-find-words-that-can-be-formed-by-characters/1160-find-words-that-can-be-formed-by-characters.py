class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        char_count = Counter(chars)
        
        for word in words:
            word_count = Counter(word)   
            
            for c in word_count:
                if word_count[c] > char_count[c]: break
            else: res += len(word)
                    
                
        return res