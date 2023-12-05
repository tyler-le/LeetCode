class Solution:
    def numberOfMatches(self, n: int) -> int:
                
        acc = 0
        
        while n > 1:
            if n % 2:
                acc+=((n-1) // 2)
                n=((n-1)//2)+1
            else:
                acc+=(n//2)
                n=(n//2)
                
        return acc
                