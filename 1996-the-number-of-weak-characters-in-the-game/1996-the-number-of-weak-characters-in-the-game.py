class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res = 0
        n = len(properties)
        max_def = 0
        properties.sort(key = lambda x : (x[0], -x[1]))
        
        for i in range(n-1, -1, -1):
            curr_def = properties[i][1]
            
            if curr_def < max_def: res+=1
            max_def = max(max_def, curr_def)
        
        return res
            