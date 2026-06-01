class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        
        target = sum(matchsticks) // 4
        if target * 4 != sum(matchsticks): return False
        matchsticks.sort(reverse=True)
        @cache
        def backtrack(index, left, up, right, down):
            if left == target and up == target and right == target and down == target: 
                return True

            if left > target or up > target  or right > target or down > target: 
                return False

            num = matchsticks[index]

            if backtrack(index + 1, left + num, up, right, down): return True
            if backtrack(index + 1, left, up + num, right, down): return True
            if backtrack(index + 1, left, up, right + num, down): return True
            if backtrack(index + 1, left, up, right, down + num): return True

            return False

        return backtrack(0, 0, 0, 0, 0)

