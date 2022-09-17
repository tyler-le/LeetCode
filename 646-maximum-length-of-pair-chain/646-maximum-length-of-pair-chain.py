class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda i : i[1])
        res = 1
        curr_end = pairs[0][1]
        
        for start, end in pairs[1:]:
            if start > curr_end: 
                res+=1
                curr_end = end
                
        return res
            