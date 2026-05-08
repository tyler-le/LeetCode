class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:


        """
        Two prefix sums that have the same remainder is a factor of k

        WHY?

        Let a = q1 * k + r1
            b = q2 * k + r2

        Then a-b = (q1k + r1) - (q2k + r2)
                 = q1*k + r1 - q2*k + r2

        IF r1 == r2, then we get:

                 = q1*k - q2*k
                 = (q1-q2) * k
                 
        which is a factor of k!
        """
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