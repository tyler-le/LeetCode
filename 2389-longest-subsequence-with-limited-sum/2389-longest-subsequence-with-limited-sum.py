class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        acc = 0
        prefix = []
        nums.sort()
        res = []
        
        for num in nums:
            acc+=num
            prefix.append(acc)
        
        for query in queries:
            res.append( bisect_right(prefix, query) )
            
        return res