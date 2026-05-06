class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum+=num
            res+=freq[curr_sum - k]
            freq[curr_sum]+=1
        
        return res
