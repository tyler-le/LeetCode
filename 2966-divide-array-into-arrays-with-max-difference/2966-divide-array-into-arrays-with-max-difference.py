class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        res = [[nums[0]]]
        n = len(nums)
        
        for num in nums[1:]:
            curr_arr = res[-1]
            
            if num - curr_arr[0] <= k and len(curr_arr) < 3:
                res[-1].append(num)
            else:
                if len(res[-1]) != 3: return []
                res.append([num])
                
        return res
            
            