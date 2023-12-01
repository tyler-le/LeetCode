class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l+=1
                r-=1
                
            return True
        
        
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return check_palindrome(l+1, r) or check_palindrome(l, r-1)
                
            l+=1
            r-=1
            
        return True