class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for ch in str(bin(n)):
            if ch == '1':
                res+=1
        return res