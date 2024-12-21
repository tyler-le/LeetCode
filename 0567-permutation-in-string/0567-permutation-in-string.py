class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of length len(s1)
        hmap = dict()
        l = 0
        s1_cnt = Counter(s1)

        for r in range(len(s2)):
            if s2[r] in hmap: hmap[s2[r]]+=1
            else: hmap[s2[r]] = 1

            while r-l+1 > len(s1):
                hmap[s2[l]]-=1
                if hmap[s2[l]] == 0: del hmap[s2[l]]
                l+=1
            
            if hmap == s1_cnt: return True

        return False
            