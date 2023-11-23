class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        res = [True for _ in range(len(l))]
        
        for i, (left, right) in enumerate(zip(l, r)):
            subarray = nums[left:right+1]
            subarray.sort()
            
            if len(subarray) == 1 or len(subarray) == 0:
                break
                
            diff = subarray[1] - subarray[0]
            for j in range(1, len(subarray)):
                if (subarray[j] - subarray[j-1]) != diff:
                    res[i] = False
                    break
        return res
                
        
            
            