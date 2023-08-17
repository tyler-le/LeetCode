class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = set()
        
        nums.sort()
        
        def recurse(sublist):
            if len(sublist) == 0:
                return
                
            # calculate average
            mini, maxi = sublist[0], sublist[-1]
            average = (mini + maxi) / 2
            
            # put in set
            averages.add(average)
            
            # recurse
            recurse(sublist[1:-1])
            
        recurse(nums)
        
        return len(averages)