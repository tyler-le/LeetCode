class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hmap = defaultdict(list)
        n = len(wordsDict)

        for i, word in enumerate(wordsDict):
            self.hmap[word].append(i)
            
        

    def shortest(self, word1: str, word2: str) -> int:
        print(f"{word1} -> {self.hmap[word1]}")
        print(f"{word2} -> {self.hmap[word2]}")

        arr1, arr2 = self.hmap[word1], self.hmap[word2]
        p1, p2 = 0, 0
        n, m = len(arr1), len(arr2)
        res = math.inf

        while p1 < n and p2 < m:

            # get the current result
            curr_dist = abs(arr1[p1] - arr2[p2])
            res = min(res, curr_dist)

            # increment left pointer
            if arr1[p1] < arr2[p2]:
                p1+=1

            # increment right pointer
            elif arr1[p1] > arr2[p2]:
                p2+=1
        
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)