class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        
        res = defaultdict(int)
        
        acc = 0
        for i, num in enumerate(nums):
            acc+=num
            for query in queries:
                if acc <= query:
                    res[query] = max(res[query], i+1)
            
                
        return [res[query] for query in queries]
            