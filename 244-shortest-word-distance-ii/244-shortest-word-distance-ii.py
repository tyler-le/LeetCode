class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hmap = collections.defaultdict(list)
        
        for index, word in enumerate(wordsDict):
            self.hmap[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        list1, list2 = self.hmap[word1], self.hmap[word2]
        l = r = 0
        res = float('inf')
        
        while l < len(list1) and r < len(list2):
            res = min(res, abs(list1[l] - list2[r]))
            if list1[l] < list2[r]: l+=1
            else: r+=1
                
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)