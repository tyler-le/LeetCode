class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        hmap = defaultdict(list)

        for person, group_size in enumerate(groupSizes):
            groups = hmap[group_size]
            
            if not groups or len(groups[-1]) == group_size:
                groups.append([person])
            else:
                groups[-1].append(person)
                        

        res = []

        for group in hmap.values():
            res.extend(group)
        return res