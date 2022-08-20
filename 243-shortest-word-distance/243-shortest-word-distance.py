class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        hmap = collections.defaultdict(list)
        
        # map word : list of indices (naturally sorted)
        for i, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                hmap[word].append(i)
            
        # get the lists of indices corresponding to 
        word1_positions, word2_positions = hmap[word1], hmap[word2]
        
        l = r = 0
    
        # find min distance between two sorted lists using two pointers
        while l < len(word1_positions) and r < len(word2_positions):
            res = min(res, abs(word1_positions[l] - word2_positions[r]))
            if word1_positions[l] < word2_positions[r]: l+=1
            else: r+=1
        
        return res
    
        
        
        
                    