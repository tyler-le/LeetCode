class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        # backtrack(i) returns the palindromes partitions from i:
        def backtrack(index, path):
            nonlocal res
            
            if index >= n:
                res.append(path.copy())
                return

            for i in range(index, n):
                prefix = s[index : i+1]
                if prefix == prefix[::-1]:
                    path.append(prefix)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return res
