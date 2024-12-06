class Solution:
    def isFascinating(self, n: int) -> bool:
        arr = list(str(n) + str(2*n) + str(3*n))
        
        arr.sort()
        
        return arr == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]