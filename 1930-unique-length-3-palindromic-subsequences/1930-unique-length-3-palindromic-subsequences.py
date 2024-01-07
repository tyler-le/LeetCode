class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        earliest = [float("inf") for _ in range(26)]
        latest = [-float("inf") for _ in range(26)]
        res = 0
        
        for i in range(len(s)):
            ch = ord(s[i]) - ord("a")
            earliest[ch] = min(i, earliest[ch])
            latest[ch] = max(i, latest[ch])
        
        for c in ascii_lowercase:
            idx = ord(c) - ord("a")
            start, end = earliest[idx], latest[idx]
            if start == float("inf") or end == -float("inf"):
                continue
                
            uniques = set()

            for i in range(start+1, end):
                uniques.add(s[i])
            
            res+=len(uniques)
        
        return res
            
        
        