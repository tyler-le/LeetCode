class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        perm = Counter(s1)
        count = {}
        
        l = 0
        for r in range(len(s2)):
            count[s2[r]] = 1 + count.get(s2[r], 0)
            
            if r-l+1 > len(s1): 
                count[s2[l]] -= 1
                if count[s2[l]] == 0: del count[s2[l]]
                l+=1
                    
            if dict(perm) == count: return True
            
        return False
                