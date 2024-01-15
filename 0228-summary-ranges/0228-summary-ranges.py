class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums: return []
        n = len(nums)
        interval, res = [nums[0], nums[0]], []
        
        for i in range(1, n):
            if nums[i] == interval[1] + 1:
                interval[1] = nums[i]
            else:
                if interval[0] != interval[1]: 
                    res.append(f"{interval[0]}->{interval[1]}")
                else: 
                    res.append(str(interval[0]))
                
                interval = [nums[i], nums[i]]
                
        if interval[0] != interval[1]: res.append(f"{interval[0]}->{interval[1]}")  
        else: res.append(str(interval[0]))

        return res
                
            
            
            