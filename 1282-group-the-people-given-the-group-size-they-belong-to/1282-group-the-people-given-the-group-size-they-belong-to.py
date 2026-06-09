class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        hmap = defaultdict(list)

        for person, group_size in enumerate(groupSizes):
            groups = hmap[group_size]
            added_to_group = False
            for group in groups:
                if len(group) < group_size:
                    group.append(person)
                    added_to_group = True
                    break
            if not added_to_group: 
                groups.append([person])
                        

        res = []

        for group in hmap.values():
            res.extend(group)
        return res