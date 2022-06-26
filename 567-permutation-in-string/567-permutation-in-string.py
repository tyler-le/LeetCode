class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count= {}, {}        
        
        # populate s1_count
        for s in s1:
            s1_count[s] = 1 + s1_count.get(s,0)
            
        # get all substrings of length s1 in s2
        substrings = []
        for i in range(len(s2) - len(s1) + 1):
            substrings.append(s2[i:i+len(s1)])
            
            
        # check each substring to see if its an anagram of s1
        for substr in substrings:
            substr_dict = {}
            for ch in substr:
                substr_dict[ch] = 1 + substr_dict.get(ch, 0)
            if substr_dict == s1_count:
                return True
            
        return False
                
                    
                    
            
        
        
            
        
        
        
        
        