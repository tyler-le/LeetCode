class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # create a list of fractions and map them to [numerator, denominator]
        
        # create an array [(fraction, [numerator, denominator])]
        
        n = len(arr)
        res = []
        
        for i in range(n):
            for j in range(i+1, n):
                res.append((arr[i] / arr[j], [arr[i], arr[j]]))
                
        res.sort()
        
        return res[k-1][-1]
                