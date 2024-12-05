class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        
        for x in arr:
            if cnt[x] == 1:
                k-=1
            if not k: 
                return x
        return ""