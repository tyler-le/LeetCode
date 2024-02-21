from typing import List
from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = []
        res = []
        acc = 0
        
        for num in nums:
            acc += num
            prefix_sum.append(acc)
        
        for query in queries:
            index = bisect_right(prefix_sum, query)
            res.append(index)
        
        return res
