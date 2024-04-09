class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        res = 0
        i = 0
        n = len(tickets)
        while tickets[k]:
            if tickets[i]:
                tickets[i]-=1
                res+=1
            i = (i+1) % n
            
        return res
                