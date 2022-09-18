class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        '''
        Intuition: dp[i] is the longest increasing subsequence that ends with the i'th element
        
        Hence, for each element, we can find the longest increasing subsequence that ends in that element and store that result in dp (dp[i] is the longest increasing subsequence that ends in the i'th element).
        
        As we go thru the inner loop from j = 0...i, if nums[i] > nums[j] then we can take the answer for dp[j] and append nums[i] to that sequence, hence increasing the sequence length by 1 (dp[j] + 1). 
        
        This means if (dp[j] + 1) is our new max for dp[i], then we will replace dp[i] with that value. otherwise keep it
        
        '''
        
        # base case - each element is an increasing sequence of length 1
        dp = [1 for _ in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                # if nums[i] is bigger, then we can append nums[i] to this subsequence
                # so we take the current answer for the sequence ending in nums[j] (aka dp[j]), and add 1 to it.
                if nums[i] > nums[j]: 
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

