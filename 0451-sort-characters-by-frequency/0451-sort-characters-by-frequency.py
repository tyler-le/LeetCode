class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        res = ""
        
        # each index i is the frequency of all the characters in that bucket
        buckets = [[] for _ in range(n+1)]
        
        hmap = Counter(s)
        
        for ch, freq in hmap.items():
            buckets[freq].append(ch)
        
        for i in range(n, -1, -1):
            for ch in buckets[i]:
                res+=(ch*i)
                
        return res
        
        
        