class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainders = {}
        remainders[0] = -1
        acc = 0


        for i, num in enumerate(nums):
            acc+=num

            if (acc % k) in remainders:
                if i - remainders[acc % k] >= 2:
                    return True
            
            else:
                remainders[acc % k] = i


        
        return False