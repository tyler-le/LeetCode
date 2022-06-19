class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums [j-1]:
                    continue

                l,r = j+1, len(nums)-1

                while l < r:
                    curr_sum = nums[l] + nums[i] + nums[j] + nums[r]
                    #print(nums[i], nums[j], nums[l], nums[r])
                    if curr_sum < target:
                        l+=1
                    elif curr_sum > target:
                        r-=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
        return res