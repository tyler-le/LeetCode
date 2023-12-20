class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = collections.defaultdict(int)
        res = 0
        
        for num in nums:
            complement = k - num
            if complement in cnt:
                res+=1
                cnt[complement]-=1
                if not cnt[complement]: del cnt[complement]
                    
            else:
                cnt[num]+=1
        
        return res