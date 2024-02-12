class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # sort based on sum of row then index of row
        
        buckets = defaultdict(list)
        res = []
        
        for i, row in enumerate(mat):
            buckets[sum(row)].append(i)
        
        for v in buckets.values():
            v.sort()
        
        for i in range(101):
            indices = buckets[i]
            if indices:
                if k > len(indices):
                    res+=indices
                    k-=len(indices)
                else:
                    res+=indices[:k]
                    return res
        return res