class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = Counter(s)
        
        arr = [(cnt,ch) for (ch,cnt) in freqs.items()]
        arr.sort(reverse=True)
        res = ""
        for freq, ch in arr:
            res+=ch * freq
        return res
        
        