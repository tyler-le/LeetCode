class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(combination, cands):

            curr_sum = sum(combination)
            
            if curr_sum == target: 
                res.append(combination.copy())
                return
            
            elif curr_sum > target: 
                return
            
            else:
                for i in range(len(cands)):
                    combination.append(cands[i])
                    helper(combination, cands[i:])
                    
                    # backtrack step
                    combination.pop()

                
        
        helper([], candidates)
        return res