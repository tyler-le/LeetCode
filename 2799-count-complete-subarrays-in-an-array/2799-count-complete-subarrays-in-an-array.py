class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l = 0
        res = 0
        n = len(nums)
        hmap = defaultdict(int)
        k = len(Counter(nums))
        for r in range(n):
            hmap[nums[r]]+=1
            
            while len(hmap) == k:
                hmap[nums[l]]-=1
                if not hmap[nums[l]]: del hmap[nums[l]]
                l+=1
                
                # The operation res += len(nums) - r is used to update the count of complete subarrays by taking into account all possible extensions of the current subarray [l...r] towards the right.
                
                # this is because if nums[l:r] is complete, then any extension past index r will also yield in a complete subarray
                res += len(nums) - r 
                
        return res
            
            
            
            