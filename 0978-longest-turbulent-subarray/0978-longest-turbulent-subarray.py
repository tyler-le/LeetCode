class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        res, cnt = 0, 0
        
        for i in range(len(arr)):
    
            if i >= 2 and (arr[i-2] < arr[i-1] > arr[i] or arr[i-2] > arr[i-1] < arr[i]):
                cnt+=1
                    
            elif i >= 1 and arr[i] != arr[i-1]:
                cnt = 2
        
            else:
                cnt = 1
                
            res = max(res, cnt)
            
        return res