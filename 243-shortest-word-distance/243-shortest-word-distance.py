class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        
        hmap = collections.defaultdict(list)
        
        for i, word in enumerate(wordsDict):
            hmap[word].append(i)
            
        l1, l2 = hmap[word1], hmap[word2]
        
        l = r = 0
        
        while l < len(l1) and r < len(l2):
            res = min(res, abs(l1[l] - l2[r]))
            if l1[l] < l2[r]: l+=1
            else: r+=1
        
        return res
    
        
        
        
                    