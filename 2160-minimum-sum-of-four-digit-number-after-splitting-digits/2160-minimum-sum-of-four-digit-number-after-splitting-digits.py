class Solution:
    def minimumSum(self, num: int) -> int:
        s = list(str(num))
        s.sort()
        
        num1 = (int(s[0]) * 10) + int(s[2])
        num2 = (int(s[1]) * 10) + int(s[3])
        
        return num1 + num2
            