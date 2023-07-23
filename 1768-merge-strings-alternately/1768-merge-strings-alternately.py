class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
       
        i, j = 0, 0
        count = 0
        word3 = ""
        
        while i < len(word1) and j < len(word2):
            # odd iter
            if count % 2: 
                word3+=word2[j]
                j+=1
            
            # even iter
            else: 
                word3+=word1[i]
                i+=1
            
            count+=1
            
        if i == len(word1): word3+=word2[j:]
        elif j == len(word2): word3+=word1[i:]
        
        return word3
                
            
            
            