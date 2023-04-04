class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        l, r, out = 0, len(people)-1, 0
        
        while l <= r:
            if people[l] + people[r] > limit:
                r-=1
            else:
                l+=1
                r-=1
            
            # out gets incremented in both cases
            # in the 'if', person r will get their own boat
            # in the 'else', persons l,r will share
            out+=1
                
        return out