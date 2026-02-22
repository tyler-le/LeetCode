
from math import factorial
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        res = 0
        curr = n
        while curr:
            res+=(factorial(curr%10))
            curr = curr // 10


        return Counter(str(res)) == Counter(str(n))
