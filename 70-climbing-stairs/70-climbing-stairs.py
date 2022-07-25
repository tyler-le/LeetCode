class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        memoized = [0 for _ in range(n+1)]
        memoized[0], memoized[1], memoized[2] = 0,1,2
        
        res = 0
        for i in range(3, n+1):
            memoized[i] = (memoized[i-2] + memoized[i-1])
            
        print(memoized)
        return memoized[n]