class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        arr2 = deque(arr2)
        
        for j in range(len(arr2)):
            curr = arr2.popleft()
            
            for i in range(len(arr1)):
                if arr1[i] == curr:
                    res.append(arr1[i])
                    
            arr1 = [value for value in arr1 if value != curr]
    
        if len(arr1) != 0:
            arr1.sort()
        return res + arr1
            
                    