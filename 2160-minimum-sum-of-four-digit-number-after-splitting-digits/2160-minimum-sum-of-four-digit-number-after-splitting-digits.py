class Solution:
    def minimumSum(self, num: int) -> int:
        s = list(str(num))
        s.sort()
        num1, num2 = [], []
        for i in range(1, len(s), 2):
            num1.append(s[i-1])
            num2.append(s[i])
        
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        
        return num1 + num2
            