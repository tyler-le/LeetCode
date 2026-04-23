class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []

        def find_differences(s1, s2):
            differences = 0
            for ch1, ch2 in zip(s1, s2):
                if ch1 != ch2: differences+=1
            
            return differences

        for query in queries:
            for word in dictionary:
                if find_differences(query, word) <= 2:
                    res.append(query)
                    break
        return res