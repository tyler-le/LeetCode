class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = list(Counter(arr).values())
        cnt.sort()
        
        i = 0
        res = 0
        
        while k:
            if not cnt[i]: 
                i+=1
            else:
                cnt[i]-=1
                k-=1
        
        for f in cnt:
            if f: res+=1
        return res