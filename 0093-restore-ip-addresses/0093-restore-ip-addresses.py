class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        n = len(s)
        res = []

        def is_valid(segment):
            if len(segment) > 3: return False
            if segment.startswith("0") and len(segment) > 1: return False
            x = int(segment)
            if not (0 <= x <= 255): return False
            return True


        def backtrack(start, path):
            nonlocal res

            # base case
            if start == n:
                if len(path) == 4:
                    res.append(".".join(path.copy()))
                return

            # recursive calls
            for end in range(start, n):
                prefix = s[start : end + 1]
                if is_valid(prefix):
                    path.append(prefix)
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res
