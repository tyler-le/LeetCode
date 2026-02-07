class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        low = 1
        high = max(candies)

        def can_distribute(pile):

            cnt = 0
            for candy in candies:
                cnt+=candy//pile
                if cnt >= k: return True
            
            return False


        while low <= high:

            mid = (high + low) // 2

            if can_distribute(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high if high > 0 else 0

        return high