class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        n = len(candies)
        res = [False for _ in range(n)]
        for i in range(n):
            if candies[i] + extraCandies >= maxi:
                res[i] = True
        return res