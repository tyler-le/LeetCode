class Solution:
    def frequencySort(self, s: str) -> str:
        # frequency of characters is limited by 26*2 total characters, so we can use bucket sort
        
        
        # arr[i] = list of characters with frequency i
        # traverse arr in reverse to build output
        
        
        cnt = Counter(s)
        res = ""
        arr = [[] for _ in range(len(s)+1)]
        
        for ch, freq in cnt.items():
            arr[freq].append(ch)
            
        for i in range(len(arr)-1, -1, -1):
            if not arr[i]: continue
            
            for x in arr[i]:
                res+=(x*i)
                
        return res