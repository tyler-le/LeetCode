class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        l = 0
        n = len(nums)
        interval = [nums[0], nums[0]]
        res = []
        
        for r in range(1, n):
            if nums[r] == interval[1] + 1:
                interval[1] = nums[r]
            else:
                if interval[0] != interval[1]:
                    res.append(f"{interval[0]}->{interval[1]}")
                
                else:
                    res.append(str(interval[0]))
                
                interval = [nums[r], nums[r]]
                
        if interval[0] != interval[1]:
            res.append(f"{interval[0]}->{interval[1]}")
                
        else:
            res.append(str(interval[0]))

        return res
                
            
            
            