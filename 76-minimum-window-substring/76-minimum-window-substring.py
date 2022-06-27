class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r,res,min_len,t_map,s_map = 0,0,[],float('inf'),{},{}
        
        for ch in t:
            t_map[ch] = 1+t_map.get(ch, 0)
        
        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            
            is_valid = True
            for key, value in t_map.items():
                if key not in s_map or s_map[key] < value:
                    is_valid = False
                
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
        print (res)
        return "" if len(res) < 2 else s[res[0]:res[1]+1]
        