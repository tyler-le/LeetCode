class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = []
        res = ["" for _ in range(n)]
        
        for athlete, pts in enumerate(score):
            arr.append((pts, athlete))
        
        arr.sort(reverse=True)
        
        for ind, (pts, athlete) in enumerate(arr):
            if ind == 0:
                res[athlete] = "Gold Medal"
            elif ind == 1:
                res[athlete] = "Silver Medal"
            elif ind == 2:
                res[athlete] = "Bronze Medal"
            else:
                res[athlete] = str(ind+1)
        
        return res
        
            