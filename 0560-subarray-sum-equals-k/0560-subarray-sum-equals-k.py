class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = collections.defaultdict(int)
        pre_sum = 0
        res = 0
        hmap[0] = 1

        for num in nums:
            pre_sum+=num
            if pre_sum - k in hmap:
                res+=hmap[pre_sum-k]
            hmap[pre_sum]+=1
        return res
            
        