class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Intuition: For each char in s, we can expand from the center and count the number of palindromes with that char as the center. We do this for all such chars.
        '''
        def count(i):
            num_palindromes = 0
            
            # find num of odd length palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_palindromes+=1
                l-=1
                r+=1
                
            # find num of even length palindromes
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_palindromes+=1
                l-=1
                r+=1
                
            return num_palindromes
        
        
        res = 0
        for i in range(len(s)):
            res+=count(i)
            
        return res