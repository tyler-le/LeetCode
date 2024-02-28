class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # hashmap[student id] -> list of scores
        
        hmap = defaultdict(list)
        res = []
        
        for student, score in items:
            heappush(hmap[student], score)
            if len(hmap[student]) > 5: heappop(hmap[student])
            
        for student, scores in hmap.items():
            res.append([student, sum(scores) // 5])
        
        res.sort(key = lambda x : x[0])
        return res
            