class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count, s2_count, l, substrs = Counter(s1), {}, 0, []
        
        for r in range(len(s2)):
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            while r-l+1 > len(s1):
                s2_count[s2[l]]-=1
                l+=1
            substrs.append(s2[l:r+1])
        
        for substr in substrs:
            if s1_count == Counter(substr): return True
        return False