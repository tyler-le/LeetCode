class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        res = ""
        
        for ch in order: 
            if ch in cnt:
                res+=(ch * cnt[ch])
                del cnt[ch]
        
        for ch, freq in cnt.items():
            res+=(ch * cnt[ch])
        return res
            