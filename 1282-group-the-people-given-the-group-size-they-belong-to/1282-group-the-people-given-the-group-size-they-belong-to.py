class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # map group size -> list of groups
        
        hmap = defaultdict(list)
        res = []
        
        for i in range(len(groupSizes)):
            gs = groupSizes[i]
            
            hmap[gs].append(i)
            
            if len(hmap[gs]) == gs:
                res.append(hmap[gs])
                hmap[gs] = []
        
        return res