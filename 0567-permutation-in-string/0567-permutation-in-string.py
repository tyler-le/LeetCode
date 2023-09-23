class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of size len(s1) + hashmap
        
        s1_map = Counter(s1)
        s2_map = Counter()
        window_size = len(s1)
        
        l = 0
        for r in range (len(s2)):
            s2_map[s2[r]]+=1
            while r-l+1 > window_size:
                s2_map[s2[l]]-=1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l+=1
            if s1_map == s2_map:
                return True
        return False