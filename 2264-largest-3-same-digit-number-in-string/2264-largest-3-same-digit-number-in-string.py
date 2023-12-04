class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        
        num = [ch for ch in num]
        for i in range(len(num) - 2):
            first, second, third = num[i], num[i+1], num[i+2]
            if first == second == third:
                res = max(res, int(first))
        
        return str(res)*3 if res >= 0 else ""