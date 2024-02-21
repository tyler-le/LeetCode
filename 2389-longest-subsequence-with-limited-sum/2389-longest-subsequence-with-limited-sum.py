class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        
        for query in queries:
            prefix_sum , count = 0, 0
            
            for num in nums:
                if prefix_sum + num <= query:
                    prefix_sum+=num
                    count+=1
            res.append(count)
                    
        return res