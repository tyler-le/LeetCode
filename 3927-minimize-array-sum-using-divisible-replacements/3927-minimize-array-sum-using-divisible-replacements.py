class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        min_value = {} # maps value -> minimum it can become

        def get_divisors(num):
            out = []
            for i in range(1, 1 + ceil(sqrt(num))):  
                if num % i == 0:
                    out.append(i)
                    out.append(num // i)  
            return out


        res = 0
        for num in nums:
            divisors = get_divisors(num)
            best = num
            for div in divisors:
                if div in min_value:
                    best = min(best, min_value[div])

            min_value[num] = best
            res+=best
        
        return res
            
            

