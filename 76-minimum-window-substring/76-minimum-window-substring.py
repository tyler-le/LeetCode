class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        res, min_len = [], float('inf')
        t_map, s_map = Counter(t), {}
        
        
        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            
            is_valid = True
            
            # check if valid
            for key, value in t_map.items():
                if key not in s_map or s_map[key] < value:
                    is_valid = False
                
            # shrink window until no longer valid and record min
            while is_valid:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res=[l,r]
                    
                s_map[s[l]]-=1
                
                if s_map[s[l]] == 0:
                    del s_map[s[l]]
                    
                for key, value in t_map.items():
                    if key not in s_map or s_map[key] < value:
                        is_valid = False
                
                l+=1
                
        return "" if len(res) == 0 else s[res[0]:res[1]+1]