class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = max(candies)
        res = []
        for candy in candies:
            res.append(candy + extraCandies >= greatest)
            
        return res