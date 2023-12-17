class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # dp[i] = number of binary trees we can make with the root at i
        
        dp = defaultdict(int)
        n = len(arr)
        
        arr.sort()
        
        for num in arr:
            dp[num] = 1
        
        
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    factor = arr[i] // arr[j]
                    if factor in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[factor]
                    
        return sum(dp.values()) % (10**9 + 7)
            