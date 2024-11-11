class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        res = 0

        for num in nums:
            
            curr = num

            # start of sequence
            if curr - 1 not in seen:
                cnt = 0
                
                while curr in seen:
                    cnt+=1
                    curr+=1

                res = max(res, cnt)
                
        return res

