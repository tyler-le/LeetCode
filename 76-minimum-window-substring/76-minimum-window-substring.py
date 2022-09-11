class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        
        # [min window len, left index, right index]
        res = [float('inf'), -1, -1]
        window, t_map, l = collections.defaultdict(int), Counter(t), 0
        
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        conditions_met = 0
        required = len(t_map) # how many conditions need to be met

        for r in range(len(s)):
            # extend the window
            window[s[r]]+=1
            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                conditions_met+=1
            
            while l <= r and conditions_met == required:
                # update min
                if r-l+1 < res[0]:
                    res = [r-l+1, l, r]
                    
                # shrink window
                window[s[l]]-=1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    conditions_met-=1
                l+=1
            
        
        return "" if [res[1], res[2]] == [-1, -1] else s[res[1]: res[2] + 1]
