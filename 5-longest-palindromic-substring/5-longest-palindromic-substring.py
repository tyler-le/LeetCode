class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = [0,0]
        
        for index in range (len(s)):
            l=r=index
            
            while l >=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    res[0], res[1] = l,r
                l-=1
                r+=1
                    
            l,r = index, index+1
            while l>= 0 and r<len(s) and s[l]==s[r]:
                if r-l+1>max_len:
                    max_len=r-l+1
                    res[0], res[1] = l,r
                l-=1
                r+=1
                    
        return s[res[0]:res[1]+1]
        