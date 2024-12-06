class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        sumi = 0
        cnt = 0
        banned = set(banned)
        
        for i in range (1, n+1):
            if i in banned: continue
            
            sumi+=i
            cnt+=1
            
            if sumi > maxSum: return cnt-1
        
        return cnt