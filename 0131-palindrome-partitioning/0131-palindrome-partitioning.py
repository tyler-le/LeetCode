class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtrack(start) processes all possible prefixes starting at s[start]. 
        # i.e. if s = "aab" and start = 0, all possible prefixes are "a", "aa", "aab". 
        # For each of these prefixes, if it is a palindrome, then we recursively process the suffix 

        cache = {}

        # backtrack(start) processes all possible prefixes starting at s[start]. 
        def backtrack(start):

            res = []

            if start >= len(s):
                return [[]]

            if start in cache: return cache[start]

            for end in range(start, len(s)):
                # For each of these prefixes, if it is a palindrome, then we recursively process the suffix 
                prefix = s[start:end+1]

                if prefix == prefix[::-1]:    
                    for result in backtrack(end+1):
                        res.append([prefix] + result)

            cache[start] = res
            return res

            
        return backtrack(0)

