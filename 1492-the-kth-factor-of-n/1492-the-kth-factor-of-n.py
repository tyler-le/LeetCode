class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1, n+1):
            if (n % i) == 0:
                res.append(i)
        
        print(res)
        return res[k-1] if k-1 < len(res) else -1
                