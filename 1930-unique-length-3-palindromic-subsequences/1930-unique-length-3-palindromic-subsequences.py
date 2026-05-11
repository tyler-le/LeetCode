class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_chars = set(s)

        first = {}
        last = {}

        res = 0

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
                last[ch] = i
            
            else:
                last[ch] = i

        for ch in unique_chars:
            start, end = first[ch], last[ch]
            letters_in_between = set()
            
            for i in range(start+1, end):
                letters_in_between.add(s[i])
            
            res+=len(letters_in_between)
        
        return res