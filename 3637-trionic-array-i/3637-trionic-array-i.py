class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        
        state = "invalid"
        n = len(nums)
        l, r = 0, 1

        # find first increasing segment
        while r < n and nums[r] > nums[r-1]:
            state = "first increasing"
            r+=1

        if state == "invalid": 
            return False
        
        # find decreasing segment
        l = r - 1
        while r < n and nums[r] < nums[r-1]:
            state = "decreasing"
            r+=1

        if state != "decreasing":
            return False

        # find second increasing segment
        l = r - 1
        while r < n and nums[r] > nums[r-1]:
            state = "second increasing"
            r+=1
        
        # valdiate
        return r == n and state == "second increasing"
            
