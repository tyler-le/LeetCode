class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hmap = Counter(arr1) + Counter(arr2) + Counter(arr3)
        res = []
        
        for x in arr1: 
            if hmap[x] == 3:
                res.append(x)
        
        return res
            