class Solution:
    def countSubstrings(self, s: str) -> int:
        # for each position, check if it is part of a palindrome
        
        def check_even(i):
            cnt = 0
            j = i
            
            while i >= 0 and j < n and s[i] == s[j]:
                cnt+=1
                i-=1
                j+=1
            
            return cnt
        
        def check_odd(i):
            cnt = 0
            j = i+1
            while i >= 0 and j < n and s[i] == s[j]:
                cnt+=1
                i-=1
                j+=1
                
            return cnt
        
        n = len(s)        
    
        return sum(check_even(i) + check_odd(i) for i in range(n)) 
            