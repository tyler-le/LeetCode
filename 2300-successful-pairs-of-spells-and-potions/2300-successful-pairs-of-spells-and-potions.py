class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()

        out = [0] * len(spells)

        for i in range(len(spells)):
            lo = 0
            hi = len(potions)
            while lo < hi:
                mid = (lo + hi) // 2
                if spells[i] * potions[mid] >= success:
                    hi = mid
                else:
                    lo = mid + 1
            out[i] = len(potions) - lo

        return out