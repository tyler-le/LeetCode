class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # update triplets greedily as long as it doesn't go over max

        res = [0,0,0]

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                res[0] = max(res[0], x)
                res[1] = max(res[1], y)
                res[2] = max(res[2], z)
        
        return res == target