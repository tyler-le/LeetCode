class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        odd_min, odd_max = math.inf, -math.inf

        odd_possible = True
        even_possible = True

        for x in nums1:
            if x % 2: 
                odd_min = min(odd_min, x)
                odd_max = max(odd_max, x)

        # try all odd
        for x in nums1:

            # if even - try to make odd (even - odd = odd)
            if not x % 2:
                if x != odd_min and x - odd_min >= 1:
                    continue
                elif x != odd_max and x - odd_max >= 1:
                    continue
                else:
                    odd_possible = False
                    break

        # try even
        for x in nums1:
            # if odd - try to make even (odd - odd = even)
            if x % 2:
                if x != odd_min and x - odd_min >= 1:
                    continue
                elif x != odd_max and x - odd_max >= 1:
                    continue
                else:
                    even_possible = False
                    break

        return odd_possible or even_possible