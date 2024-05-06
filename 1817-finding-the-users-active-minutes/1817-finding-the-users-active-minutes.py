class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # map user -> set of times
        
        hmap = defaultdict(set)
        res = [0 for _ in range(k)]
        for user, time in logs:
            hmap[user].add(time)
        
        for st in hmap.values():
            res[len(st) - 1]+=1
        
        return res
        