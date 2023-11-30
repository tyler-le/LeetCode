class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = res = 0
        
        for ch in s:
            if ch == "R": count+=1
            else: count-=1
            
            if not count: res+=1
                
        return res
            