class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        # sliding window of length k
        res = 0
        l = 0
        arr = list(str(num))
        n = len(arr)
        
        
        for r in range(n):
            
            while r-l+1 > k:
                l+=1
            
            if r-l+1 == k:
                s_x = arr[l:r+1]
                x = int("".join(s_x))
                
                if x and not num % x: 
                    res+=1
        
        return res
                    