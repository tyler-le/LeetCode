class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): 
            return -1

        def can_make(day):
            num_bouquets = 0
            l = 0
            for r in range(len(bloomDay)):
                if bloomDay[r] > day: 
                    l = r + 1
                else:
                    if r - l + 1 == k:
                        num_bouquets+=1
                        l = r + 1
            return num_bouquets >= m
        
        low, high = min(bloomDay), max(bloomDay)

        while low < high:
            mid = (high + low) // 2
            if can_make(mid): high = mid
            else: low = mid + 1
        return high
