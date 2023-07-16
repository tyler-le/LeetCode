class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0, [-1,-1]]
        
        def palindrome_helper(i):
    
            res = [0, [-1,-1]]
            
            # check odd length palindromes
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                if r-l-1 > res[0]:
                    res[1] = [l+1, r-1]
                    
            res[0] = max(res[0], r-l-1)
                
            # check even length palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                if r-l-1 > res[0]:
                    res[1] = [l+1, r-1]
            res[0] = max(res[0], r-l-1)
            
            return res
                
                
        for i in range(len(s)):
            
            count, pos = palindrome_helper(i)
            if count > res[0]:
                res[0] = count
                res[1] = pos
            
            
        
        return s[res[1][0]:res[1][1]+1]
            