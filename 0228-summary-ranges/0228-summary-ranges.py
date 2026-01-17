class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r, n, res = 0, 0, len(nums), []


        while r < n:
            l = r

            while (r + 1 < n) and nums[r] + 1 == nums[r+1]:
                r+=1
            
            if l == r: res.append(f"{nums[l]}")
            else: res.append(f"{nums[l]}->{nums[r]}")
            r+=1
        
        return res
            
        

