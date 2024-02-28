class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # hashmap[student id] -> list of scores
        
        hmap = defaultdict(list)
        res = []
        
        for student, score in items:
            hmap[student].append(score)
            
        for student, scores in hmap.items():
            scores.sort()
            res.append([student, sum(scores[-5:]) // 5])
        
        res.sort(key = lambda x : x[0])
        return res
            