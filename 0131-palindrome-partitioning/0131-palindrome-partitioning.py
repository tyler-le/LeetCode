class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # at each step, we can append to each choice or we can make a new str

        def backtrack(start):

            res = []

            if start >= len(s):
                return [[]]

            for i in range(start, len(s)):
                prefix = s[start:i+1]
                if prefix == prefix[::-1]:
                    for result in backtrack(i+1):
                        res.append([prefix] + result)
            
            return res

            
        return backtrack(0)

