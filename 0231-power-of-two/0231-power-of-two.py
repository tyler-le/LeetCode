class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return math.log2(n) % 1 == 0
        