class Solution:
    def minDeletions(self, s: str) -> int:
        # ceabaacb
        # aaabbbcce
        
        count = collections.Counter(s)
        seen_counts = set()
        res = 0
                
        for key, value in count.items():
            while value != 0 and value in seen_counts:
                res+=1
                value-=1
            seen_counts.add(value)
        
        return res
        
                
                
            
            