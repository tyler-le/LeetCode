class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        arr = []
        for num_passengers, src, dst in trips:
            arr.append((num_passengers, src))
            arr.append((-num_passengers, dst))
        
        arr.sort(key = lambda x : (x[1], x[0]))
        
        cnt = 0
        for magnitude, _ in arr:
            cnt+=magnitude
            if cnt > capacity: return False

        return True

