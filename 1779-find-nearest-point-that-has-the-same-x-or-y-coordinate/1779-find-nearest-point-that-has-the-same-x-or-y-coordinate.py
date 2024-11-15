class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        res = -1
        
        for i, (x2, y2) in enumerate(points):
            dist = abs(x-x2) + abs(y-y2)

            if (x == x2 or y == y2) and dist < min_distance:
                min_distance = dist
                res = i
        
        return res