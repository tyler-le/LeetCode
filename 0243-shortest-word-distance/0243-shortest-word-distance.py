class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # makes = [1, 4]
        # coding = [3]
        
        w1 = [i for i in range(len(wordsDict)) if wordsDict[i] == word1]
        w2 = [i for i in range(len(wordsDict)) if wordsDict[i] == word2]
        res = math.inf
        for i in w1:
            for j in w2:
                res = min(res, abs(i-j))
        
        return res
            