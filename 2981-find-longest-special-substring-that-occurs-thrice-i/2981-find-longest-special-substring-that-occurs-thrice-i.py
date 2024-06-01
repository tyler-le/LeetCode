class Solution:
    def maximumLength(self, s: str) -> int:
        # sliding window of fixed length 1...n
        # each sliding window iteration -> map substring to number of occurrences
        # filter substrings that occur >= 3 times
        # record max length one
        
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
        res = -1
        for i in range(1, n):
            sliding_window(i)
        
        return res
        
