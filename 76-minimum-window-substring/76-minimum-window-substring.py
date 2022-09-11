class Solution:
    def minWindow(self, s: str, t: str) -> str:
 
        # [min window len, left index, right index]
        res = [float('inf'), -1, -1]
        
        window, t_map, l = collections.defaultdict(int), Counter(t), 0
        
        # e.g. if t is "AABC" then the window must have two A's, one B and one C.           Thus conditions_met would be = 3 when all these conditions are met.
        conditions_met = 0
        
        # how many total conditions need to be met
        required = len(t_map) 

        for r in range(len(s)):
            # extend the window
            window[s[r]]+=1
            
            # check if s[r] causes a met condition
            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                conditions_met+=1
            
            # shrink window until conditions arent met
            while l <= r and conditions_met == required:
                # update res
                if r-l+1 < res[0]: res = [r-l+1, l, r]
                    
                window[s[l]]-=1
                
                # check if removing s[l] causes a condition to be un-met
                if window[s[l]] < t_map[s[l]]:
                    conditions_met-=1
                    
                l+=1
            
        
        return "" if [res[1], res[2]] == [-1, -1] else s[res[1]: res[2] + 1]
