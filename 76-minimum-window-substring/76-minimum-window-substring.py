class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        '''
        Checks if all chars in t_map are in s_map
        '''
        def is_valid(s_map, t_map):
            # checks if t_map is a subset of s_map
            flag = True
            for key, value in t_map.items():
                if key not in s_map or s_map[key] < value: 
                    flag = False
            return flag
            
            
        
        min_window_len = float('inf')
        min_window_pos = [-1, -1]
        s_map, t_map, l = collections.defaultdict(int), Counter(t), 0

        for r in range(len(s)):
            # extend the window
            s_map[s[r]]+=1
            
            while is_valid(s_map, t_map):
                # update min
                if r-l+1 < min_window_len:
                    min_window_len = r-l+1
                    min_window_pos = [l, r]
                    
                # shrink window
                s_map[s[l]]-=1
                if s_map[s[l]] == 0: del s_map[s[l]]
                l+=1
            
        
        return "" if min_window_pos == [-1, -1] else s[min_window_pos[0]: min_window_pos[1] + 1]
