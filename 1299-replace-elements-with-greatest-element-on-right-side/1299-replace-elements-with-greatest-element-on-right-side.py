class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = arr[-1]
        
        for i in range(len(arr)-1, 0, -1):
            maxi = max(arr[i], maxi)
            arr[i] = maxi
            
        arr.append(-1)
        return arr[1:]
        