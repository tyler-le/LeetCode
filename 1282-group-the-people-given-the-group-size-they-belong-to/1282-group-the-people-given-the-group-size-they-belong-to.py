class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # at the least, there is 1 group
        # at the most, there are n groups
        
        # groupSizes = [2,1,3,3,3,2,4,4]
        
        # |Group Size| == 1 -> P1
        # |Group Size| == 2 -> P0, P5, P6, P7
        # |Group Size| == 3 -> P2, P3, P4
        
        # map "Group Size" : [People]
        hmap = collections.defaultdict(list)
        
        for i in range(len(groupSizes)):
            person, size = i, groupSizes[i]
            hmap[size].append(person)
            
        res = []

        for groupSize, peoples in hmap.items():
            count = 0
            grouping = []
            
            for person in peoples:
                
                grouping.append(person)
                count+=1
                
                if count == groupSize:
                    res.append(grouping)
                    count = 0
                    grouping = []
        
        return res
                
            
            
        