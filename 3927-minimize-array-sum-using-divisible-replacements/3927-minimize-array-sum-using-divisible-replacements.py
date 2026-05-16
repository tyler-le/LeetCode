class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        min_value = {} # maps value -> minimum it can become

        def get_divisors(num):
            out = set()  
            for i in range(1, int(math.isqrt(num)) + 1):  
                if num % i == 0:
                    out.add(i)
                    out.add(num // i)  
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
            
            

