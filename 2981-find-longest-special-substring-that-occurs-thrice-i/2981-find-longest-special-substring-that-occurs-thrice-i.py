class Solution:
    def maximumLength(self, s: str) -> int:
        # sliding window 
        # map a -> [list of all special substrings for 'a']
        # filter result to all hmap.values() that are >= 3
        # take max length one
        
        def sliding_window(k):
            nonlocal res
            l = 0
            n = len(s)
            curr = deque()
            cnt = defaultdict(int)
            
            
            for r in range(n):
                curr.append(s[r])
                
                while r-l+1 > k or s[r] != s[l]:
                    curr.popleft()
                    l+=1
                
                if r-l+1 == k and s[r] == s[l]:
                    cnt["".join(curr)]+=1
            
            
            for substr, occ in cnt.items():
                if occ >= 3:
                    res = max(res, len(substr))
                    
        n = len(s)
        st = set()
        res = -1
        for i in range(1, n):
            sliding_window(i)
        
        return res
        
