class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        res = set()
        
        for num in nums:
            cnt[num]+=1
            if cnt[num] > n //3: 
                res.add(num)
        return list(res)