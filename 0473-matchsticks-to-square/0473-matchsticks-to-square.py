class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # four choices for one matchstick
        # valid case - all 4 sides have the same sum - sum  // 4

        matchsticks.sort(reverse=True)

        if sum(matchsticks) % 4: return False

        target = sum(matchsticks) // 4
        n = len(matchsticks)
        cache = {}


        def backtrack(index, left, right, top, bottom):
            nonlocal target, n

            if (index, left, right, top, bottom) in cache:
                return cache[(index, left, right, top, bottom)]

            if left > target or right > target:
                return False
            
            if top > target or bottom > target:
                return False

            if left == target and right == target and top == target and bottom == target: return True

            if index == n: return False

            match = matchsticks[index]

            # place ith match in left position
            try_left = backtrack(index + 1, left + match, right, top, bottom)

            # place ith match in right position
            try_right = backtrack(index + 1, left, right + match, top, bottom)

            # place ith match in top position
            try_top = backtrack(index + 1, left, right, top + match, bottom)

            # place ith match in bottom position
            try_bottom = backtrack(index + 1, left, right, top, bottom + match)

            res = try_left or try_right or try_top or try_bottom
            cache[(index, left, right, top, bottom)] = res

            return res

        return backtrack(0, 0, 0, 0, 0)