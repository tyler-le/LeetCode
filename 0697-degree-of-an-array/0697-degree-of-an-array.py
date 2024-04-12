class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = defaultdict(int)
        cnt = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            if num not in left: left[num] = i
            right[num] = i
            cnt[num]+=1
            
        res = len(nums)
        degree = max(Counter(nums).values())
        for num in nums:
            if cnt[num] == degree:
                res = min(res, right[num] - left[num] + 1)
        
        return res
        
            
        
            