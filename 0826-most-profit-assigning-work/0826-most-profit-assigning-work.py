class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        
        # greedily assign workers to highest profit job within their difficulty using binary search
    
        
        res = 0
        jobs = [(diff, prof) for prof, diff in zip(profit, difficulty)]
        jobs.sort(key = lambda x : x[0])
        worker.sort()
        i = 0
        best = 0
        
        for ability in worker:
            
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i+=1
            
            res+=best
            
        return res