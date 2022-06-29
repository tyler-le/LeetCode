class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
        arr.sort()
        
        l,min_diff = 0, float('inf')
        res = []
        
        for r in range(1, len(arr)):
            diff = abs(arr[r] - arr[l])
            
            if diff <= min_diff:
                
                # found a new diff, so reset
                if diff < min_diff:
                    del res[:]
                    min_diff = diff
                res.append([arr[l], arr[r]])
                
            l+=1
        
        return res
        
        
        