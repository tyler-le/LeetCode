class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def f(index, path):
            if len(path) == k:
                res.append(path.copy())
                return
            
            if index > n: 
                return

            # include
            f(index + 1, path + [index])

            # exclude
            f(index + 1, path)

        f(1, [])
        return res

        