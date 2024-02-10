class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def check_even(i):
            cnt = 0
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                cnt+=1
                left-=1
                right+=1
            return cnt
        
        def check_odd(i):
            cnt = 0
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                cnt+=1
                left-=1
                right+=1
            return cnt
            
        
        res = 0
        n = len(s)
        for i in range(n):
            # even length
            res+=check_even(i)
            
            # odd length
            res+=check_odd(i)
        
        return res