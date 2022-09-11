class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        '''
        Checks if all chars in t_map are in s_map
        '''
        def is_valid(window, t_map):
            # checks if t_map is a subset of s_map
            flag = True
            for key, value in t_map.items():
                if key not in window or window[key] < value: 
                    flag = False
            return flag
        
        # [min window len, left index, right index]
        res = [float('inf'), -1, -1]
        window, t_map, l = collections.defaultdict(int), Counter(t), 0
        
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        conditions_met = 0

        for r in range(len(s)):
            # extend the window
            window[s[r]]+=1
            
            while is_valid(window, t_map):
                # update min
                if r-l+1 < res[0]:
                    res[0] = r-l+1
                    res[1], res[2] = l, r
                    
                # shrink window
                window[s[l]]-=1
                if window[s[l]] == 0: del window[s[l]]
                l+=1
            
        
        return "" if [res[1], res[2]] == [-1, -1] else s[res[1]: res[2] + 1]
